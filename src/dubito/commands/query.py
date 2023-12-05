import requests_cache
from datetime import timedelta
import logging
import validators
from dubito.subito_list_page import SubitoListPage, SubitoListPageQuery, subito_list_page_items_dataframe
from rich.logging import RichHandler
from os import path, mkdir
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from dubito.subito_list_page_filter import BaseSubitoListPageFilter
from dubito.filters import MinimumPriceSubitoListPageFilter, MaximumPriceSubitoListPageFilter, TitleContainsIncludeSubitoLiistPageFilter, TitleContainsExcludeSubitoLiistPageFilter, RemoveOutliersSubitoListPageFilter

from dubito import models

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
    else:
        if not validators.url(url):
            raise Exception(f'"{url}" is not a valid url, You must specify a valid url.')
        subito_list_page = SubitoListPage(url)

    x = models.SubitoListPage(url=subito_list_page.url, query=subito_list_page.query)

    # Convert the downloaded items to a pandas dataframe and applies some filters

    df = subito_list_page_items_dataframe(subito_list_page)

    x.save()
    # Iterate over the dataframe rows
    for index, row in df.iterrows():
        subito_insertion = models.SubitoInsertion(
            title=row['title'],
            url=row['url'],
            thumbnail=row['thumbnail'],
            price=row['price'],
            city=row['city'],
            state=row['state'],
            subito_list_page=x
        )
        subito_insertion.save()
