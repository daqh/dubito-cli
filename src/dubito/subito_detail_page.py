from datetime import datetime
from selectorlib import Extractor
from dubito.utils import simplified_get, extractors_directory
import logging

class SubitoDetailPage:
    '''Represents a Subito detail page.
    
    Attributes
    ----------
    url : str
        The URL of the detail page.
    identifier : str
        The identifier of the detail page.
    '''
    
    def __init__(self, url: str):
        '''Initializes a new instance of the SubitoDetailPage class.
        
        Parameters
        ----------
        url : str
            The URL of the detail page.
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
    
class ExtractedSubitoDetailPage(SubitoDetailPage):
    '''Represents an extracted Subito detail page.
    
    Attributes
    ----------
    url : str
        The URL of the detail page.
    response : str
        The response of the detail page.
    '''

    def __init__(self, subito_detail_page: SubitoDetailPage, response_text: str) -> None:
        '''Initializes a new instance of the ExtractedSubitoDetailPage class.
        
        Parameters
        ----------
        subito_detail_page : SubitoDetailPage
            The Subito detail page.
        response_text : str
            The response of the detail page.
        '''
        super().__init__(subito_detail_page.url)
        self.__response_text = response_text

    @property
    def response_text(self):
        return self.__response_text

class TransformedSubitoDetailPage(ExtractedSubitoDetailPage):
    '''Represents a transformed Subito detail page.
    
    Attributes
    ----------
    url : str
        The URL of the detail page.
    response : str
        The response of the detail page.
    subito_detail_page_item : dict
        The item of the detail page.
    '''

    def __init__(self, extracted_subito_detail_page: ExtractedSubitoDetailPage, subito_detail_page_item: dict) -> None:
        '''Initializes a new instance of the TransformedSubitoDetailPage class.

        Parameters
        ----------
        extracted_subito_detail_page : ExtractedSubitoDetailPage
            The extracted Subito detail page.
        subito_detail_page_item : dict
            The item of the detail page.
        '''
        super().__init__(extracted_subito_detail_page, extracted_subito_detail_page.response)
        self.__subito_detail_page_item = subito_detail_page_item

    @property
    def subito_detail_page_item(self):
        return self.__subito_detail_page_item

def extract_subito_detail_page(subito_detail_page: SubitoDetailPage) -> ExtractedSubitoDetailPage:
    '''Extracts a Subito detail page.
    
    Parameters
    ----------
    subito_detail_page : SubitoDetailPage
        The Subito detail page.
    '''
    logging.info(f"Extracting {subito_detail_page}")
    response_text = simplified_get(subito_detail_page.url)
    return ExtractedSubitoDetailPage(subito_detail_page, response_text)

__subito_detail_page_extractor = Extractor.from_yaml_file(f"{extractors_directory}/subito_detail_page.yml")

def transform_subito_detail_page(extracted_subito_detail_page: ExtractedSubitoDetailPage) -> TransformedSubitoDetailPage:
    '''Transforms an extracted Subito detail page.
    
    Parameters
    ----------
    extracted_subito_detail_page : ExtractedSubitoDetailPage
        The extracted Subito detail page.
    '''
    subito_detail_page_item = __subito_detail_page_extractor.extract(extracted_subito_detail_page.response_text)
    subito_detail_page_item["timestamp"] = datetime.now()
    subito_detail_page_item["price"] = float(subito_detail_page_item["price"].replace("€", "").replace(".", "").replace(",", "."))
    subito_detail_page_item["shipping_available"] = bool(subito_detail_page_item["shipping_available"])
    subito_detail_page_item["sold"] = bool(subito_detail_page_item["sold"])
    subito_detail_page_item["city"] = subito_detail_page_item["location"].split()[0]
    subito_detail_page_item["state"] = subito_detail_page_item["location"].split()[1]
    subito_detail_page_item["identifier"] = extracted_subito_detail_page.identifier
    del subito_detail_page_item["location"]
    return TransformedSubitoDetailPage(extracted_subito_detail_page, subito_detail_page_item)

def extract_and_transform_subito_detail_page(subito_detail_page: SubitoDetailPage) -> TransformedSubitoDetailPage:
    '''Extracts and transforms a Subito detail page.
    
    Parameters
    ----------
    subito_detail_page : SubitoDetailPage
        The Subito detail page.
    '''
    extracted_subito_detail_page = extract_subito_detail_page(subito_detail_page)
    transformed_subito_detail_page = transform_subito_detail_page(extracted_subito_detail_page)
    return transformed_subito_detail_page
