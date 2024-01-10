import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sys import stdin
from rich import print
import mplfinance as mpf
from deep_translator import GoogleTranslator
import ta

from dubito.models import NewspaperArticle
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import os

def analyze(keywords: list[str]):
    df = pd.read_csv(stdin, parse_dates=["created_at"])

    # Format the condition column truncating the string at " - " and getting the first part

    # Remove outliers by interquartile range
    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    df = df[(df["price"] > (q1 - 1.5 * iqr)) & (df["price"] < (q3 + 1.5 * iqr))]

    df["page"] = df.groupby("slp_id").ngroup() + 1

    report_folder = "report"
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    with open(os.path.join(report_folder, 'report.md'), 'w') as f:
        f.write('# Report\n')
        for keyword in keywords:
            f.write(f'1. {keyword}\n')

    print(df.describe())

    sns.countplot(data=df, x="state", order=df["state"].value_counts().index)
    plt.xticks(rotation=90, fontsize=3)
    plt.savefig(os.path.join(report_folder, "state_distribution.png"))
    # Questa distribuzione segue una power law
    # Calcola la percentuale di record per ogni stato
    plt.clf()

    colors = sns.color_palette("deep")
    sns.displot(df, x="price", hue="condition", kde=True, palette=colors)
    for i, condition in enumerate(df["condition"].unique()):
        plt.axvline(df[df["condition"] == condition]["price"].mean(), color=colors[i], linestyle="dashed", linewidth=1.5)
    plt.savefig(os.path.join(report_folder, "price_condition_distribution.png"))
    plt.clf()
    sns.countplot(data=df, x="condition", hue="condition", order=df["condition"].value_counts().index, legend=True)
    plt.xlabel("Condition")
    plt.ylabel("Count")
    plt.xticks([])
    plt.tight_layout()
    plt.savefig(os.path.join(report_folder, "condition_count.png"))
    plt.clf()

    sns.countplot(data=df, x="sold", hue="condition")
    plt.ylabel("Count")
    plt.xticks(ticks=[0, 1], labels=["Unsold", "Sold"])
    plt.tight_layout()
    plt.savefig(os.path.join(report_folder, "condition_sold_count.png"))
    plt.clf()

    df["condition"] = df["condition"].str.split(" - ").str[0]
    # Calculate the percentage of sold over unsold for each condition
    condition_counts = df.groupby("condition")["sold"].value_counts(normalize=True).unstack()
    condition_counts.plot(kind="bar", stacked=True)
    plt.xlabel("Condition")
    plt.ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.legend(["Unsold", "Sold"])
    plt.tight_layout()
    plt.savefig(os.path.join(report_folder, "sold_percentage_by_condition.png"))
    plt.clf()

    sns.displot(df, x="price", hue="shipping_available", kde=True, multiple="stack")
    # Calculate the mean of the price for each shipping_available value and plot it as a vertical line
    plt.axvline(df[df["shipping_available"] == False]["price"].mean(), color="blue", linestyle="dashed", linewidth=1)
    plt.axvline(df[df["shipping_available"] == True]["price"].mean(), color="red", linestyle="dashed", linewidth=1)
    plt.savefig(os.path.join(report_folder, "price_shipping_available_distribution.png"))
    plt.clf()

    sns.jointplot(data=df, x="page", y="price", kind="hex", color="darkblue")
    plt.xlabel("Page")
    plt.ylabel("Price")
    plt.axhline(df["price"].describe()["75%"], color="black", linestyle="dashed", linewidth=1)
    plt.text(0, df["price"].describe()["75%"], "75%", color="black", fontsize=15, weight="bold")
    plt.axhline(df["price"].describe()["50%"], color="white", linestyle="dashed", linewidth=1)
    plt.text(0, df["price"].describe()["50%"], "50%", color="white", fontsize=15, weight="bold")
    plt.axhline(df["price"].describe()["25%"], color="white", linestyle="dashed", linewidth=1)
    plt.text(0, df["price"].describe()["25%"], "25%", color="white", fontsize=15, weight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(report_folder, "page_price.png"))
    plt.clf()

    sns.displot(df, x="price", hue="sold", kde=True, multiple="stack", legend=False)
    plt.xlabel("Price")
    # Calculate the mean of the price for each sold value and plot it as a vertical line
    plt.axvline(df[df["sold"] == False]["price"].mean(), color="blue", linestyle="dashed", linewidth=1, label="Unsold Mean")
    plt.axvline(df[df["sold"] == True]["price"].mean(), color="red", linestyle="dashed", linewidth=1, label="Sold Mean")
    plt.axvline(df.describe()["price"]["25%"], color="gray", linestyle="dashed", linewidth=1)
    plt.legend(["Sold", "Unsold", "Unsold Mean", "Sold Mean", "25%, 50%, 75%"])
    plt.axvline(df.describe()["price"]["50%"], color="gray", linestyle="dashed", linewidth=1)
    plt.axvline(df.describe()["price"]["75%"], color="gray", linestyle="dashed", linewidth=1)
    plt.savefig(os.path.join(report_folder, "price_distribution.png"))
    print("Media prezzo venduti", df[df["sold"] == True]["price"].mean())
    print("Media prezzo invenduti", df[df["sold"] == False]["price"].mean())
    print("Mediana", df["price"].median())
    print("Rapporto prezzo venduti/invenduti", df[df["sold"] == True]["price"].mean()/df[df["sold"] == False]["price"].mean())
    # Conta il numero di invenduti tra il 25% e il 50%
    print("Invenduti tra 25% e 50%", len(df[(df["price"] > df.describe()["price"]["25%"]) & (df["price"] < df.describe()["price"]["50%"]) & (df["sold"] == False)]))
    # Conta il numero di venduti tra il 25% e il 50%
    print("Venduti tra 25% e 50%", len(df[(df["price"] > df.describe()["price"]["25%"]) & (df["price"] < df.describe()["price"]["50%"]) & (df["sold"] == True)]))
    
    with open(os.path.join(report_folder, 'report.md'), 'a') as f:
        f.write('## Price distribution\n')
        f.write(f'Price mean: **{df["price"].mean()}**\n\n')
        f.write(f'Price median: **{df["price"].median()}**\n\n')
        f.write(f'Price std: **{df["price"].std()}**\n\n')
        f.write('---\n\n')
        f.write(f'Price mean (sold): **{df[df["sold"] == True]["price"].mean()}**\n\n')
        f.write(f'Price median (sold): **{df[df["sold"] == True]["price"].median()}**\n\n')
        f.write(f'Price std (sold): **{df[df["sold"] == True]["price"].std()}**\n\n')
        f.write('---\n\n')
        f.write(f'Price mean (not sold): **{df[df["sold"] == False]["price"].mean()}**\n\n')
        f.write(f'Price median (not sold): **{df[df["sold"] == False]["price"].median()}**\n\n')
        f.write(f'Price std (not sold): **{df[df["sold"] == False]["price"].std()}**\n\n')

        f.write('![Price distribution](price_distribution.png)')

    df.dropna(inplace=True, subset=["created_at"])
    df.sort_values(by=["created_at"], inplace=True)

    freq = "4d"

    grouper = pd.Grouper(key="created_at", freq=freq)
    candles = df.groupby(grouper)

    # Create a dataframe with open, close, high and low
    candles = pd.DataFrame(
        data={
            "open": candles["price"].first(),
            "high": candles["price"].max(),
            "low": candles["price"].min(),
            "close": candles["price"].last(),
            "volume": candles["price"].count(),
            'created_at': candles['created_at'].first(),
        },
    )
    candles.set_index("created_at", inplace=True)

    candles.dropna(inplace=True)

    ad = ta.volume.acc_dist_index(candles["high"], candles["low"], candles["close"], candles["volume"], fillna=True)
    force_index = ta.volume.force_index(candles["close"], candles["volume"], window=7)
    macd = ta.trend.macd(candles["close"], window_slow=26, window_fast=12, fillna=True)
    macd_diff = ta.trend.macd_diff(candles["close"], window_slow=26, window_fast=12, window_sign=9, fillna=True)
    macd_signal = ta.trend.macd_signal(candles["close"], window_slow=26, window_fast=12, window_sign=9, fillna=True)
    dpo = ta.trend.dpo(candles["close"], window=20, fillna=True)

    exp = None
    for keyword in keywords:
        if exp is None:
            exp = NewspaperArticle.title.contains(keyword) | NewspaperArticle.text.contains(keyword)
        else:
            exp = exp | NewspaperArticle.title.contains(keyword) | NewspaperArticle.text.contains(keyword)

    articles = NewspaperArticle.filter(exp)
    # Parse articles to pd DataFrame

    stx = " ".join([a.title.lower() for a in articles])
    wc = WordCloud(
        stopwords=stopwords.words("italian")
    ).generate(stx)
    wc.to_file(os.path.join(report_folder, "wordcloud.png"))
    with open(os.path.join(report_folder, 'report.md'), 'a') as f:
        f.write('## Wordcloud\n![Wordcloud](wordcloud.png)\n')

    translator = GoogleTranslator(source="it", target="en")
    sia = SentimentIntensityAnalyzer()

    articles = pd.DataFrame.from_records([a.__data__ for a in articles], exclude=["id"])
    articles = articles.dropna(subset=["publish_date"])

    with open(os.path.join(report_folder, 'report.md'), 'a') as f:
        f.write('## Articles\n')
        f.write(f'**{len(articles)}** article/s found\n')
        for article in articles.sort_values(by=["publish_date"], ascending=False).itertuples():
            f.write(f'1. {article.publish_date} | [{article.title}]({article.url})\n')

    # print(f'Translating {len(articles)} articles...')
    # # Translate article titles to english
    # articles["title"] = translator.translate_batch(articles["title"].tolist())
    # # Calculate sentiment
    # articles["compound"] = articles["title"].apply(lambda x: sia.polarity_scores(x)["compound"])

    articles = articles.groupby(pd.Grouper(key="publish_date", freq="1d"))
    articles = articles.count()
    # # Make the df dates match the candle dates
    articles = articles.reindex(df.groupby(pd.Grouper(key="created_at", freq="1d")).count().dropna().index.date, fill_value=0)
    # # Parse articles index to datetime
    articles.index = pd.to_datetime(articles.index)
    articles = articles.groupby(pd.Grouper(freq=freq)).sum()
    articles = articles.reindex(candles.index.date, fill_value=0)

    # Create the addplot using the marker array
    addplot = [
        # mpf.make_addplot(articles, type="bar", markersize=100, marker="^", color="green", panel=2, ylabel="Articles"),
        # mpf.make_addplot(ad, panel=3, ylabel="Accumulation/Distribution", color="orange"),
        # mpf.make_addplot(force_index, panel=3, ylabel="Force Index"),
        mpf.make_addplot(macd_diff, panel=2, ylabel="MACD diff", type="bar", color=["green" if x >= 0 else "red" for x in macd_diff]),
        mpf.make_addplot(macd, panel=2, ylabel="MACD"),
        mpf.make_addplot(macd_signal, panel=2, ylabel="MACD signal", color="orange"),
    ]

    # Add vertical line at the day 22 september 2023
    plt.axvline(x=pd.to_datetime('2023-09-22'), color='red', linestyle='--')

    mpf.plot(candles, type="candle", style="yahoo", volume=True, savefig="report/price_candles.png", mav=(7, 9, 28), addplot=addplot, tight_layout=True, vlines=dict(vlines=['2023-09-12', '2023-09-15', '2023-09-22'], linewidths=1.5, colors="gray", alpha=1, linestyle="dashed"))

    with open('report/report.md', 'a') as f:
        f.write('## Price candles\n![Price candles](price_candles.png)\n')
