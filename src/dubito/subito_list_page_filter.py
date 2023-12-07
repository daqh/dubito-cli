import pandas as pd
from abc import ABC, abstractmethod
from typing import Optional

@DeprecationWarning
class SubitoListPageFilter(ABC):
    '''Filter for subito list page items.'''

    @abstractmethod
    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        '''Filter subito list page items.
        
        Parameters
        ----------
        subito_list_page_items : pd.DataFrame
            The subito list page items.

        Returns
        -------
        pd.DataFrame
            The filtered subito list page items.
        '''
        pass

    @abstractmethod
    def handle(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        '''Handle subito list page items.

        Parameters
        ----------
        subito_list_page_items : pd.DataFrame
            The subito list page items.

        Returns
        -------
        pd.DataFrame
            The handled subito list page items.
        '''
        pass

class BaseSubitoListPageFilter(SubitoListPageFilter):
    '''Base class for subito list page filters.'''

    def __init__(self, next_filter: Optional[SubitoListPageFilter] = None):
        '''Initializes a new instance of the BaseSubitoListPageFilter class.

        Parameters
        ----------
        next_filter : Optional[SubitoListPageFilter], optional
            The next filter, by default None
        '''
        self.__next_filter = next_filter

    @property
    def next_filter(self) -> Optional[SubitoListPageFilter]:
        return self.__next_filter
    
    @next_filter.setter
    def next_filter(self, next_filter: Optional[SubitoListPageFilter]):
        self.__next_filter = next_filter
    
    def filter(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        '''Filter subito list page items.
        
        Parameters
        ----------
        subito_list_page_items : pd.DataFrame
            The subito list page items.
            
        Returns
        -------
        pd.DataFrame
            The filtered subito list page items.
        '''
        return subito_list_page_items

    def handle(self, subito_list_page_items: pd.DataFrame) -> pd.DataFrame:
        '''Handle subito list page items.

        Parameters
        ----------
        subito_list_page_items : pd.DataFrame
            The subito list page items.

        Returns
        -------
        pd.DataFrame
            The handled subito list page items.
        '''
        filtered = self.filter(subito_list_page_items)
        if self.__next_filter is not None:
            return self.__next_filter.handle(filtered)
        else:
            return filtered
