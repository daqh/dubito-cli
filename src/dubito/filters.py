import pandas as pd
from typing import Optional
from dubito.subito_list_page_filter import BaseSubitoListPageFilter

class MinimumPriceSubitoListPageFilter(BaseSubitoListPageFilter):

    def __init__(self, minimum_price: float, next_filter: Optional[BaseSubitoListPageFilter] = None):
        super().__init__(next_filter)
        self.__minimum_price = minimum_price

    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        df = subito_list_page_items[subito_list_page_items["price"] >= self.__minimum_price]
        return df

class MaximumPriceSubitoListPageFilter(BaseSubitoListPageFilter):

    def __init__(self, maximum_price: float, next_filter: Optional[BaseSubitoListPageFilter] = None):
        super().__init__(next_filter)
        self.__maximum_price = maximum_price

    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        df = subito_list_page_items[subito_list_page_items["price"] <= self.__maximum_price]
        return df

class TitleContainsIncludeSubitoLiistPageFilter(BaseSubitoListPageFilter):

    def __init__(self, include: list[str], next_filter: Optional[BaseSubitoListPageFilter] = None):
        super().__init__(next_filter)
        self.__include = include

    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
            q = None
            for k in self.__include:
                if q is None:
                    q = subito_list_page_items["title"].str.contains(k, case=False)
                else:
                    q |= subito_list_page_items["title"].str.contains(k, case=False)
            if q is not None:
                subito_list_page_items = subito_list_page_items[q]
            return subito_list_page_items

class TitleContainsExcludeSubitoLiistPageFilter(BaseSubitoListPageFilter):

    def __init__(self, exclude: list[str], next_filter: Optional[BaseSubitoListPageFilter] = None):
        super().__init__(next_filter)
        self.__exclude = exclude

    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        for k in self.__exclude:
            subito_list_page_items = subito_list_page_items[~subito_list_page_items["title"].str.contains(k, case=False)]
        return subito_list_page_items

class RemoveOutliersSubitoListPageFilter(BaseSubitoListPageFilter):

    def __init__(self, r: float = 1.5, next_filter: Optional[BaseSubitoListPageFilter] = None):
        super().__init__(next_filter)
        self.__r = r

    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        q1 = subito_list_page_items['price'].quantile(0.25)
        q3 = subito_list_page_items['price'].quantile(0.75)
        iqr = q3 - q1
        r = self.__r
        subito_list_page_items = subito_list_page_items[~((subito_list_page_items['price'] < (q1 - r * iqr)) | (subito_list_page_items['price'] > (q3 + r * iqr)))]
        return subito_list_page_items
