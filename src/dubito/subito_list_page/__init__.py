from selectorlib import Extractor
from dubito.utils import simplified_get, extractors_directory
from urllib.parse import urlparse, parse_qs
from datetime import datetime
from typing import Iterator

class SubitoListPage:
    '''A Subito list page.
    
    Attributes
    ----------
    url : str
        The url of the page.
    query : str
        The query of the page.
    page_number : int
        The page number of the page.

    Methods
    -------
    __iter__()
        Returns an iterator over the pages.
    __getitem__(page_number)
        Returns the page with the given page number.
    __str__()
        Returns a string representation of the page.

    Raises
    ------
    ValueError
        If the url does not contain a query.
        If the page number is less than 1.
    '''

    def __init__(self, url) -> None:
        '''Initializes the page.
        
        Parameters
        ----------
        url : str
            The url of the page.

        Raises
        ------
        ValueError
            If the url does not contain a query.
            If the page number is less than 1.

        Examples
        --------
        >>> from dubito.subito_list_page import SubitoListPage
        >>> subito_list_page = SubitoListPage("https://www.subito.it/annunci-lazio/vendita/usato/?q=macbook+pro&o=1")
        >>> subito_list_page.url
        'https://www.subito.it/annunci-lazio/vendita/usato/?q=macbook+pro&o=1'
        '''
        self.__url = url
        parsed_url = urlparse(url)
        parsed_qs = parse_qs(parsed_url.query)
        try:
            self.__query = parsed_qs["q"][0]
        except:
            raise ValueError("The url must contain a query.")
        page_number = int(parsed_qs["o"][0] if "o" in parsed_qs.keys() else 1)
        if page_number < 1:
            raise ValueError("The page number must be greater than 0.")
        self.__page_number = int(page_number)

    @property
    def url(self) -> str:
        '''The url of the page.'''
        return self.__url
    
    @property
    def query(self) -> str:
        '''The query of the page.'''
        return self.__query
    
    @property
    def page_number(self) -> int:
        '''The page number of the page.'''
        return self.__page_number
    
    def __iter__(self) -> "SubitoListPage":
        subito_list_page = self
        while True:
            yield subito_list_page
            try:
                subito_list_page = subito_list_page[subito_list_page.page_number + 1]
            except StopIteration:
                break
    
    def __getitem__(self, page_number: int) -> "SubitoListPage":
        return SubitoListPageQuery(self.query, page_number)

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.url})"

class SubitoListPageQuery(SubitoListPage):
    '''A Subito list page with a query.
    
    Attributes
    ----------
    url : str
        The url of the page.
    query : str
        The query of the page.
    page_number : int
        The page number of the page.

    Raises
    ------
    ValueError
        If the page number is less than 1.
        If the url does not contain a query.
    '''

    __url = "https://www.subito.it/annunci-italia/vendita/usato/?q={query}&o={page_number}"

    def __init__(self, query: str, page_number: int = 1) -> None:
        '''Initializes the page.

        Parameters
        ----------
        query : str
            The query of the page.
        page_number : int, optional
            The page number of the page, by default 1.

        Raises
        ------
        ValueError
            If the page number is less than 1.
            If the url does not contain a query.
        '''
        url = self.__url.format(query=query, page_number=page_number)
        super().__init__(url)

class ExtractedSubitoListPage(SubitoListPage):
    '''A Subito list page with an extractor.
    
    Attributes
    ----------
    url : str
        The url of the page.
    query : str
        The query of the page.
    page_number : int
        The page number of the page.
    response_text : str
        The response text of the page.
        
    Raises
    ------
    ValueError
        If the page number is less than 1.
        If the url does not contain a query.
    '''

    def __init__(self, subito_list_page: SubitoListPage, response_text: str) -> None:
        '''Initializes the page.

        Parameters
        ----------
        subito_list_page : SubitoListPage
            The Subito list page.
        response_text : str
            The response text of the page.
            
        Raises
        ------
        ValueError
            If the page number is less than 1.
            If the url does not contain a query.

        Examples
        --------
        >>> from dubito.subito_list_page import SubitoListPage, ExtractedSubitoListPage
        >>> subito_list_page = SubitoListPage("https://www.subito.it/annunci-lazio/vendita/usato/?q=macbook+pro&o=1")
        >>> extracted_subito_list_page = ExtractedSubitoListPage(subito_list_page, "<html>...</html>")        
        '''
        super().__init__(subito_list_page.url)
        self.__response_text = response_text

    @property
    def response_text(self) -> str:
        '''The response text of the page.'''
        return self.__response_text
    
    def __getitem__(self, page_number: int) -> SubitoListPage:
        subito_list_page = super().__getitem__(page_number)
        extracted_subito_list_page = extract_subito_list_page(subito_list_page)
        return extracted_subito_list_page

class TransformedSubitoListPage(ExtractedSubitoListPage):
    '''A Subito list page with a transformer.
    
    Attributes
    ----------
    url : str
        The url of the page.
    query : str
        The query of the page.
    page_number : int
        The page number of the page.
    response_text : str
        The response text of the page.
    subito_list_page_items : list[dict]
        The items of the page.

    Raises
    ------
    ValueError
        If the page number is less than 1.
        If the url does not contain a query.
    '''

    def __init__(self, extracted_subito_list_page: ExtractedSubitoListPage, subito_list_page_items: list[dict]) -> None:
        '''Initializes the page.

        Parameters
        ----------
        extracted_subito_list_page : ExtractedSubitoListPage
            The extracted Subito list page.
        subito_list_page_items : list[dict]
            The items of the page.

        Raises
        ------
        ValueError
            If the page number is less than 1.
            If the url does not contain a query.s
        '''
        super().__init__(extracted_subito_list_page, extracted_subito_list_page.response_text)
        self.__subito_list_page_items = subito_list_page_items
        
    @property
    def subito_list_page_items(self):
        '''The items of the page.'''
        return self.__subito_list_page_items
    
    def __getitem__(self, page_number: int) -> SubitoListPage:
        subito_list_page = super().__getitem__(page_number)
        extracted_subito_list_page = extract_subito_list_page(subito_list_page)
        try:
            transformed_subito_list_page = transform_extracted_subito_list_page(extracted_subito_list_page)
        except ValueError:
            raise StopIteration
        return transformed_subito_list_page

def extract_subito_list_page(subito_list_page: SubitoListPage) -> ExtractedSubitoListPage:
    '''Extracts a Subito list page.
    
    Parameters
    ----------
    subito_list_page : SubitoListPage
        The Subito list page.
        
    Returns
    -------
    ExtractedSubitoListPage
        The extracted Subito list page.
    '''
    response_text = simplified_get(subito_list_page.url)
    return ExtractedSubitoListPage(subito_list_page, response_text)

__subito_list_page_extractor = Extractor.from_yaml_file(f'{extractors_directory}/subito_list_page_extractor.yaml')

def transform_extracted_subito_list_page(extracted_subito_list_page: ExtractedSubitoListPage) -> TransformedSubitoListPage:
    '''Transforms an extracted Subito list page.
    
    Parameters
    ----------
    extracted_subito_list_page : ExtractedSubitoListPage
        The extracted Subito list page.

    Returns
    -------
    TransformedSubitoListPage
        The transformed Subito list page.
    '''
    response_text = extracted_subito_list_page.response_text
    result = __subito_list_page_extractor.extract(response_text)
    subito_list_page_items = result["subito_list_page_items"]
    if not subito_list_page_items:
        raise ValueError("The Subito List Page is empty.")
    for subito_list_page_item in subito_list_page_items:
        subito_list_page_item["page"] = extracted_subito_list_page.page_number
        subito_list_page_item["timestamp"] = datetime.now()
        subito_list_page_item["shipping_available"] = "spedizione disponibile" in subito_list_page_item["price"].lower()
        if subito_list_page_item["price"]:
            subito_list_page_item["price"] = subito_list_page_item["price"].split()[0].replace(".", "").replace(",", ".")
        subito_list_page_item["identifier"] = subito_list_page_item["url"].split("-")[-1].split(".")[0]
        subito_list_page_item["sold"] = bool(subito_list_page_item["sold"])
        try:
            subito_list_page_item["price"] = float(subito_list_page_item["price"])
        except:
            subito_list_page_item["price"] = None
    return TransformedSubitoListPage(extracted_subito_list_page, subito_list_page_items)

def extract_and_transform_subito_list_page(subito_list_page: SubitoListPage) -> TransformedSubitoListPage:
    '''Extracts and transforms a Subito list page.
    
    Parameters
    ----------
    subito_list_page : SubitoListPage
        The Subito list page.

    Returns
    -------
    TransformedSubitoListPage
        The transformed Subito list page.
    '''
    extracted_subito_list_page = extract_subito_list_page(subito_list_page)
    return transform_extracted_subito_list_page(extracted_subito_list_page)

def subito_list_page_item_iterator(subito_list_page: SubitoListPage) -> Iterator[dict]:
    '''Iterates over the items of a Subito list page.

    Parameters
    ----------
    subito_list_page : SubitoListPage
        The Subito list page.

    Yields
    ------
    dict
        The item of the Subito list page.
    '''
    for transformed_subito_list_page in extract_and_transform_subito_list_page(subito_list_page):
        for subito_list_page_item in transformed_subito_list_page.subito_list_page_items:
            yield subito_list_page_item

