import pandas as pd
from abc import ABC, abstractmethod
from typing import Optional

class SubitoListPageFilter(ABC):

    @abstractmethod
    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def handle(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        pass

class BaseSubitoListPageFilter(SubitoListPageFilter):

    def __init__(self, next_filter: Optional[SubitoListPageFilter] = None):
        self.__next_filter = next_filter

    @property
    def next_filter(self) -> Optional[SubitoListPageFilter]:
        return self.__next_filter
    
    @next_filter.setter
    def next_filter(self, next_filter: Optional[SubitoListPageFilter]):
        self.__next_filter = next_filter
    
    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        return subito_list_page_items

    def handle(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        filtered = self.filter(subito_list_page_items)
        if self.__next_filter is not None:
            return self.__next_filter.handle(filtered)
        else:
            return filtered
