import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sys import stdin
import numpy as np
import logging
from rich import print
from rich.panel import Panel
from rich.columns import Columns

def analyze():
    df = pd.read_csv(stdin)
    count = df.shape[0]
    print(f"Number of listings before removing outliers: {count}")
    
    # Remove outliers from df
    df = df[np.abs(df["price"]-df["price"].mean()) <= (3*df["price"].std())]
    df_sold = df[df.sold == True]["price"]
    df_unsold = df[df.sold == False]["price"]
    count = df.shape[0]
    print(f"Number of listings after removing outliers: {count}")

    general_panel = Panel(str(df.describe()), title="General", border_style="green")
    sold_panel = Panel(str(df_sold.describe()), title="Sold", border_style="yellow")
    unsold_panel = Panel(str(df_unsold.describe()), title="Unsold", border_style="yellow")

    from rich.layout import Layout

    layout = Layout()
    layout.split_column(
        Layout(name="top"),
        Layout(name="bottom")
    )
    layout["top"].split_row(
        Layout(general_panel, name="left"),
        Layout(sold_panel, name="center"),
        Layout(unsold_panel, name="right")
    )
    print(layout)

    sns.displot(df, x="price", hue="sold", kde=True, multiple="stack")
    plt.show()
    