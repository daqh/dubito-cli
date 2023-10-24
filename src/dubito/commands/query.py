import requests_cache
from datetime import timedelta
import logging
import pandas as pd
import validators
from dubito.subito_list_page import SubitoListPage, SubitoListPageQuery, subito_list_page_item_iterator
from rich.logging import RichHandler
from os import path, mkdir
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def query(query: str, url: str, include: list[str], exclude: list[str], minimum_price: float, maximum_price: float, install_cache: bool, verbose: bool, remove_outliers: bool) -> None:

    if verbose:
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[RichHandler(markup=True)],
        )

    if install_cache:
        logging.info("Installing cache")
        requests_cache.install_cache('dubito_cache', backend="sqlite", expire_after=timedelta(hours=1))

    if query:
        subito_list_page = SubitoListPageQuery(query)
        subito_list_page_items = list(subito_list_page_item_iterator(subito_list_page))
    else:
        if not validators.url(url):
            raise Exception(f'"{url}" is not a valid url, You must specify a valid url.')
        subito_list_page = SubitoListPage(url)
        subito_list_page_items = list(subito_list_page_item_iterator(subito_list_page))

    # Convert the downloaded items to a pandas dataframe and applies some filters

    df = pd.DataFrame(subito_list_page_items).set_index("identifier")
    df = df[~df.index.duplicated(keep='first')]

    # Filer 1: Get everything under the specified price
    if minimum_price is not None:
        df = df[df["price"] >= minimum_price]

    # Filer 2: Get everything over the specified price
    if maximum_price is not None:
        df = df[df["price"] <= maximum_price]

    # Filer 3: Get everything that contains the specified keywords
    q = None
    for k in include:
        if q is None:
            q = df["title"].str.contains(k, case=False)
        else:
            q |= df["title"].str.contains(k, case=False)
    if q is not None:
        df = df[q]

    # Filer 4: Get everything that does not contain the specified keywords
    for k in exclude:
        df = df[~df["title"].str.contains(k, case=False)]

    # Filer 5: Remove outliers
    if remove_outliers:
        q1 = df['price'].quantile(0.25)
        q3 = df['price'].quantile(0.75)
        iqr = q3 - q1
        r = 1.5
        df = df[~((df['price'] < (q1 - r * iqr)) | (df['price'] > (q3 + r * iqr)))]

    # Finally, sort by price
    df = df.sort_values(by=["price"])

    # Check if "results" folder exists
    if not path.exists("results"):
        mkdir("results")

    project_name = query.replace(" ", "_") # Replace spaces with underscores in the query
    project_folder = f"results/{project_name}"

    if not path.exists(project_folder):
        mkdir(project_folder)

    now = datetime.now()

    if not path.exists(f"{project_folder}/y{now.year}"):
        mkdir(f"{project_folder}/y{now.year}")

    project_folder = f"{project_folder}/y{now.year}"

    if not path.exists(f"{project_folder}/m{now.month}"):
        mkdir(f"{project_folder}/m{now.month}")

    project_folder = f"{project_folder}/m{now.month}"

    if not path.exists(f"{project_folder}/d{now.day}"):
        mkdir(f"{project_folder}/d{now.day}")

    project_folder = f"{project_folder}/d{now.day}"

    if not path.exists(f"{project_folder}/H{now.hour}"):
        mkdir(f"{project_folder}/H{now.hour}")

    project_folder = f"{project_folder}/H{now.hour}"

    if not path.exists(f"{project_folder}/M{now.minute}"):
        mkdir(f"{project_folder}/M{now.minute}")

    project_folder = f"{project_folder}/M{now.minute}"

    # Save the dataframe to a csv file

    df.to_csv(f"{project_folder}/subito_list_page_items.csv")

    # Plot the results
    sns.displot(df, x="price", hue="sold", kde=True, multiple="stack")
    plt.xlabel("Price")
    plt.savefig(f"{project_folder}/price_distribution.png")

    df["price"].describe().to_csv(f"{project_folder}/statistics.csv")

