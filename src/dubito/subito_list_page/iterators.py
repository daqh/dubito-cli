from dubito.subito_list_page import SubitoListPage, TransformedSubitoListPage, SubitoQueryListPage
import pandas as pd

def subito_list_page_item_iterator(list_page: SubitoListPage):
    '''
    # Transformed Page Item Iterator
    Iterates over the transformed list pages from subito.it.

    Arguments
    ---------
    `list_page: SubitoListPage`
        The SubitoListPage object to iterate.

    Yields
    ------
    `insertion: dict`

    Example
    -------
    ```python
    from subito import SubitoListPage, transformed_list_page_item_iterator

    page = SubitoListPage("rtx 2080")
    for insertion in transformed_list_page_item_iterator(page):
        print(insertion)
    ```
    '''
    current_list_page = list_page
    while True:
        transformed_list_page = TransformedSubitoListPage.from_subito_list_page(current_list_page)
        if not len(transformed_list_page):
            break
        for subito_list_page_item in transformed_list_page:
            yield subito_list_page_item
        current_list_page = SubitoQueryListPage(current_list_page.query, current_list_page.page_number + 1)

def subito_list_page_item_iterator_from_query(query: str):
    '''
    # Transformed Page Item Iterator From Query
    Iterates over the transformed pages from subito.it, from a query.

    Arguments
    ---------
    `query: str`
        The query to search.

    Yields
    ------
    `insertion: dict`
    '''
    return subito_list_page_item_iterator(SubitoQueryListPage(query))

def subito_list_page_item_iterator_from_url(url: str):
    '''
    # Transformed Page Item Iterator From URL
    Iterates over the transformed pages from subito.it, from an url.

    Arguments
    ---------
    `url: str`
        The url to search.

    Yields
    ------
    `insertion: dict`
    '''
    return subito_list_page_item_iterator(SubitoListPage(url))

def subito_list_page_item_list_from_query(query: str) -> list[dict]:
    '''
    # Get Transformed Subito List Page Item From Query
    Gets a collection of insertions from a query.

    Arguments
    ---------
    `query: str`
        The query to search.

    Returns
    -------
    `list[dict]`
        The list of insertions.
    '''
    return list(subito_list_page_item_iterator_from_query(query))

def subito_list_page_item_list_from_url(url: str) -> list[dict]:
    '''
    # Get Transformed Subito List Page Item From URL
    Gets a collection of insertions from an url with duplicates.

    Arguments
    ---------
    `url: str`
        The url to search.

    Returns
    -------
    `list[dict]`
        The list of insertions.
    '''
    return list(subito_list_page_item_iterator_from_url(url))
