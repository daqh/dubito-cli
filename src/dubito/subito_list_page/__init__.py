from pyparsing import Iterator
from selectorlib import Extractor
from dubito.utils import simplified_get, extractors_directory
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class SubitoListPage:

    def __init__(self, url) -> None:
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
        return self.__url
    
    @property
    def query(self) -> str:
        return self.__query
    
    @property
    def page_number(self) -> int:
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

    __url = "https://www.subito.it/annunci-italia/vendita/usato/?q={query}&o={page_number}"

    def __init__(self, query: str, page_number: int = 1) -> None:
        url = self.__url.format(query=query, page_number=page_number)
        super().__init__(url)

class ExtractedSubitoListPage(SubitoListPage):

    def __init__(self, subito_list_page: SubitoListPage, response_text: str) -> None:
        super().__init__(subito_list_page.url)
        self.__response_text = response_text

    @property
    def response_text(self) -> str:
        return self.__response_text
    
    def __getitem__(self, page_number: int) -> SubitoListPage:
        subito_list_page = super().__getitem__(page_number)
        extracted_subito_list_page = extract_subito_list_page(subito_list_page)
        return extracted_subito_list_page

class TransformedSubitoListPage(ExtractedSubitoListPage):

    def __init__(self, extracted_subito_list_page: ExtractedSubitoListPage, subito_list_page_items: list[dict]) -> None:
        super().__init__(extracted_subito_list_page, extracted_subito_list_page.response_text)
        self.__subito_list_page_items = subito_list_page_items
        
    @property
    def subito_list_page_items(self):
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
    '''
    # Extract Subito List Page
    Extract a Subito List Page.

    Arguments
    ---------
    `subito_list_page: SubitoListPage`
        The SubitoListPage object to extract.
    '''
    response_text = simplified_get(subito_list_page.url)
    return ExtractedSubitoListPage(subito_list_page, response_text)

__subito_list_page_extractor = Extractor.from_yaml_file(f'{extractors_directory}/subito_list_page_extractor.yaml')

def transform_extracted_subito_list_page(extracted_subito_list_page: ExtractedSubitoListPage) -> TransformedSubitoListPage:
    '''
    # Transform Subito List Page
    Transform an ExtractedSubitoListPage into a TransformedSubitoListPage.

    Arguments
    ---------
    `extracted_subito_list_page: ExtractedSubitoListPage`
        The ExtractedSubitoListPage object to transform.
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
    '''
    # Extract and Transform Subito List Page
    Extract and transform a SubitoListPage into a TransformedSubitoListPage.

    Arguments
    ---------
    `subito_list_page: SubitoListPage`
        The SubitoListPage object to extract and transform.
    '''
    extracted_subito_list_page = extract_subito_list_page(subito_list_page)
    return transform_extracted_subito_list_page(extracted_subito_list_page)

def subito_list_page_item_iterator(subito_list_page: SubitoListPage) -> Iterator[dict]:
    '''
    # Subito List Page Item Iterator
    Iterate over the items of a SubitoListPage.

    Arguments
    ---------
    `subito_list_page: SubitoListPage`
        The SubitoListPage object to iterate over.
    '''
    for transformed_subito_list_page in extract_and_transform_subito_list_page(subito_list_page):
        for subito_list_page_item in transformed_subito_list_page.subito_list_page_items:
            yield subito_list_page_item

