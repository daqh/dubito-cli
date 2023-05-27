from datetime import datetime
from selectorlib import Extractor
from dubito.utils import simplified_get, extractors_directory
import logging

class SubitoDetailPage:
    '''
    # SubitoDetailPage
    A SubitoDetailPage is a page that contains the details of an insertion.

    Attributes
    ----------
    `url: str`
        The url of the page.
    '''

    def __init__(self, url: str):
        '''
        # SubitoDetailPage > Constructor
        The constructor for the SubitoDetailPage class.

        Arguments
        ---------
        `url: str`
            The url of the page.
        `identifier: str`
            The identifier of the page.
        '''
        self.__url = url
        self._identifier = self.url.split("-")[-1].split(".")[0]

    @property
    def url(self):
        return self.__url
    
    @property
    def identifier(self):
        return self._identifier

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.identifier})"

class ExtractedSubitoDetailPage:
    '''
    # ExtractedSubitoDetailPage
    An ExtractedSubitoDetailPage is a page that contains the details of an insertion and its extracted data.

    Attributes
    ----------
    `detail_page: SubitoDetailPage`
        The SubitoDetailPage object to extract.
    `response: str`
        The text of the page.
    '''

    def __init__(self, detail_page: SubitoDetailPage):
        '''
        # ExtractedSubitoDetailPage > Constructor

        Arguments
        ---------
        `detail_page: SubitoDetailPage`
            The SubitoDetailPage object to extract.
        '''
        self.__detail_page = detail_page
        logging.info(f"Extracting {self}")
        response_text = simplified_get(detail_page.url)
        self.__response = response_text
    
    @property
    def response(self):
        return self.__response
    
    @property
    def detail_page(self):
        return self.__detail_page
    
    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.detail_page})"
    
    @classmethod
    def from_url(cls, url: str):
        '''
        # ExtractedSubitoDetailPage > From URL
        Create an ExtractedSubitoDetailPage object from an url.

        Arguments
        ---------
        `url: str`
            The url of the page.

        Example
        -------
        ```python
        from subito import ExtractedSubitoDetailPage
        extracted_detail_page = ExtractedSubitoDetailPage.from_url("https://www.subito.it/vi/180882013.htm")
        ```
        '''
        return cls(SubitoDetailPage(url))

class TransformedSubitoDetailPage:
    '''
    # TransformedSubitoDetailPage
    A TransformedSubitoDetailPage is a page that contains the details of an insertion and its extracted and transformed data.

    Attributes
    ----------
    `extracted_detail_page: ExtractedSubitoDetailPage`
        The ExtractedSubitoDetailPage object to transform.
    `subito_detail_page_item: dict`
        The transformed data.
    '''

    __subito_detail_page_extractor = Extractor.from_yaml_file(f'{extractors_directory}/subito_detail_page_extractor.yaml')

    def __init__(self, extracted_detail_page: ExtractedSubitoDetailPage):
        '''
        # TransformedSubitoDetailPage > Constructor
        
        Arguments
        ---------
        `extracted_detail_page: ExtractedSubitoDetailPage`
            The ExtractedSubitoDetailPage object to transform.
        '''
        self.__extracted_detail_page = extracted_detail_page
        self.__subito_detail_page_item = self.__subito_detail_page_extractor.extract(extracted_detail_page.response)
        self.__subito_detail_page_item["timestamp"] = datetime.now()
        self.__subito_detail_page_item["price"] = float(self.__subito_detail_page_item["price"].replace("€", "").replace(".", "").replace(",", "."))
        self.__subito_detail_page_item["shipping_available"] = bool(self.__subito_detail_page_item["shipping_available"])
        self.__subito_detail_page_item["sold"] = bool(self.__subito_detail_page_item["sold"])
        self.__subito_detail_page_item["city"] = self.__subito_detail_page_item["location"].split()[0]
        self.__subito_detail_page_item["state"] = self.__subito_detail_page_item["location"].split()[1]
        self.__subito_detail_page_item["identifier"] = self.extracted_detail_page.detail_page.identifier
        del self.__subito_detail_page_item["location"]
    
    @property
    def extracted_detail_page(self):
        return self.__extracted_detail_page

    @property
    def subito_detail_page_item(self):
        return self.__subito_detail_page_item
    
    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.extracted_detail_page})"

    @classmethod
    def from_url(cls, url: str):
        '''
        # TransformedSubitoDetailPage > From URL
        Create a TransformedSubitoDetailPage object from an url.

        Arguments
        ---------
        `url: str`
            The url of the page.

        Example
        -------
        ```python
        from subito import TransformedSubitoDetailPage

        TransformedSubitoDetailPage.from_url("https://www.subito.it/vi/180882013.htm")
        '''
        return cls(ExtractedSubitoDetailPage.from_url(url))
    