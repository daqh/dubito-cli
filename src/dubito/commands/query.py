import requests_cache
from datetime import timedelta
import logging
import validators
from dubito.subito_list_page import SubitoListPage, SubitoListPageQuery, subito_list_page_item_iterator
from os import path, mkdir
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from dubito.subito_list_page_filter import BaseSubitoListPageFilter
from dubito.filters import MinimumPriceSubitoListPageFilter, MaximumPriceSubitoListPageFilter, TitleContainsIncludeSubitoLiistPageFilter, TitleContainsExcludeSubitoLiistPageFilter, RemoveOutliersSubitoListPageFilter

def query(query: str, url: str, include: list[str], exclude: list[str], minimum_price: float, maximum_price: float, install_cache: bool, remove_outliers: bool) -> None:

    if install_cache:
        logging.info("Installing cache")
        requests_cache.install_cache('dubito_cache', backend="sqlite", expire_after=timedelta(hours=1))

    if query:
        subito_list_page = SubitoListPageQuery(query)
    else:
        if not validators.url(url):
            raise Exception(f'"{url}" is not a valid url, You must specify a valid url.')
        subito_list_page = SubitoListPage(url)

    # Convert the downloaded items to a pandas dataframe and applies some filters

    for subito_list_page_item in subito_list_page_item_iterator(subito_list_page):
        subito_list_page_item.subito_list_page.save()
        logging.debug(subito_list_page_item.subito_list_page)
        subito_list_page_item.save()
        logging.debug(subito_list_page_item)
