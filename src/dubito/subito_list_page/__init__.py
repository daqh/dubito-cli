import urllib.parse
from datetime import datetime
from selectorlib import Extractor
from dubito.utils import simplified_get, extractors_directory
import logging

class SubitoListPage:
    '''
    # Subito List Page
    A class to represent a list page from subito.it.

    Attributes
    ----------
    `url: str`
        The url of the page.
    `query: str`
        The query of the page.
    `page_number: int`
        The number of the page.
    '''

    def __init__(self, url):
        '''
        # Subito List Page > Constructor
        The constructor for the SubitoListPage class.

        Arguments
        ---------
        `url: str`
            The url of the page.

        Raises
        ------
        `ValueError`
            If the url does not contain a query.
        '''
        self.__url = url
        parsed_url = urllib.parse.urlparse(url)
        parsed_qs = urllib.parse.parse_qs(parsed_url.query)
        try:
            self.__query = parsed_qs["q"][0]
        except:
            raise ValueError("The url must contain a query.")
        self.__page_number = int(parsed_qs["o"][0]) if "o" in parsed_qs.keys() else 1
    
    @property
    def url(self):
        return self.__url
    
    @property
    def query(self):
        return self.__query

    @property
    def page_number(self):
        return self.__page_number
    
    def __getitem__(self, key):
        '''
        # Subito List Page > Get Item
        Get the page with the given number.

        Example
        -------
        ```python
        from subito import SubitoListPage

        page = SubitoListPage("https://www.subito.it/annunci-italia/vendita/usato/?q=rtx%202080&o=1")
        print(page[3].url)
        # Output:
        # https://www.subito.it/annunci-italia/vendita/usato/?q=rtx%202080&o=3
        ```
        '''
        return SubitoQueryListPage(self.query, key)

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.query}, {self.page_number})"

class SubitoQueryListPage(SubitoListPage):
    '''
    # Subito Query List Page
    A class to represent a page from subito.it, with a query.
    
    By default this class produces a url in the form of:
    `https://www.subito.it/annunci-italia/vendita/usato/?q={query}&o={page_number}`

    ## Attributes
    `url: str`
        The url of the page.
    `number: int = 1`
        The number of the page.

    ## Example
    ```python
    from subito import SubitoQueryListPage

    page = SubitoQueryListPage("rtx 2080")
    print(page.url)
    ```
    '''

    __url = "https://www.subito.it/annunci-italia/vendita/usato/?q={query}&o={page_number}"

    def __init__(self, query: str, page_number: int = 1):
        url = self.__url.format(query=query, page_number=page_number)
        # Format the url
        url = urllib.parse.quote(url, safe=':/?&=')
        super().__init__(url)

class ExtractedSubitoListPage:
    '''
    # Extracted Subito List Page
    A class to represent a list page from subito.it, with the text extracted.

    ## Attributes
    `url: str`
        The url of the page.
    `text: str`
        The text of the page.
    '''

    def __init__(self, subito_list_page: SubitoListPage):
        '''
        # Extracted Subito List Page > Constructor
        The constructor for the ExtractedSubitoListPage class.

        Arguments
        ---------
        `subito_list_page: SubitoListPage`
            The SubitoListPage object to extract.
        '''
        self.__subito_list_page = subito_list_page
        logging.info(f"Extracting {subito_list_page}")
        response_text = simplified_get(subito_list_page.url)
        self.__response = response_text

    @property
    def response(self):
        return self.__response
    
    @property
    def subito_list_page(self):
        return self.__subito_list_page

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.subito_list_page})"
    
    @classmethod
    def from_url(cls, url: str):
        '''
        # Extracted Subito List Page > From URL
        Create an ExtractedSubitoListPage object from an url.

        Arguments
        ---------
        `url: str`
            The url of the page.

        Example
        -------
        ```python
        from subito import ExtractedSubitoListPage

        page = ExtractedSubitoListPage.from_url("https://www.subito.it/annunci-italia/vendita/usato/?q=rtx%202080&o=1")
        ```
        '''
        return cls(SubitoListPage(url))

    @classmethod
    def from_query(cls, query: str, page_number: int = 1):
        '''
        # Extracted Subito List Page > From Query
        Create an ExtractedSubitoListPage object from a query.

        Arguments
        ---------
        `query: str`
            The query of the page.

        Example
        -------
        ```python
        from subito import ExtractedSubitoListPage

        page = ExtractedSubitoListPage.from_query("rtx 2080")
        ```
        '''
        return cls(SubitoQueryListPage(query, page_number))

class TransformedSubitoListPage:
    '''
    # Transformed Subito List Page
    A class to represent a list page from subito.it, with the text extracted and transformed.

    Attributes
    ----------
    `url: str`
        The url of the page.
    `text: str`
        The text of the page.

    Example
    -------
    ```python
    from subito import SubitoListPage, TransformedSubitoListPage

    page = SubitoListPage("rtx 2080")
    extracted_page = ExtractedSubitoListPage(page)

    transformed_page = TransformedSubitoListPage(extracted_page)
    print(transformed_page.insertions)
    ```
    '''

    __subito_list_page_extractor = Extractor.from_yaml_file(f'{extractors_directory}/subito_list_page_extractor.yaml')

    def __init__(self, extracted_subito_list_page: ExtractedSubitoListPage):
        '''
        # Transformed Subito List Page > Constructor

        Arguments
        ---------
        `extracted_subito_list_page: ExtractedSubitoListPage`
            The ExtractedSubitoListPage object to transform.
        '''
        self.__extracted_subito_list_page = extracted_subito_list_page
        logging.info(f"Transforming {self}")
        result = self.__subito_list_page_extractor.extract(extracted_subito_list_page.response)
        self.__subito_list_page_items = result["subito_list_page_items"]
        if not self.__subito_list_page_items:
            self.__subito_list_page_items = []
        for subito_list_page_item in self.__subito_list_page_items:
            subito_list_page_item["page"] = extracted_subito_list_page.subito_list_page.page_number
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

    @property
    def subito_list_page_items(self):
        return self.__subito_list_page_items
    
    @property
    def extracted_subito_list_page(self):
        return self.__extracted_subito_list_page

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.extracted_subito_list_page})"

    @classmethod
    def from_url(cls, url: str):
        '''
        # Transformed Subito List Page > From URL
        Create a TransformedSubitoListPage object from an url.

        Arguments
        ---------
        `url: str`
            The url of the page.
        '''
        return cls(ExtractedSubitoListPage.from_url(url))

    @classmethod
    def from_query(cls, query: str, page_number: int = 1):
        '''
        # Transformed Subito List Page > From Query
        Create a TransformedSubitoListPage object from a query.

        Arguments
        ---------
        `query: str`
            The query of the page.
        '''
        return cls(ExtractedSubitoListPage.from_query(query, page_number))
