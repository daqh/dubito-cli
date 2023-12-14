import requests_cache
from datetime import timedelta
import logging
import validators
from dubito.subito_list_page import SubitoListPage, SubitoListPageQuery, subito_list_page_item_iterator
import logging
from dubito.database import db
from dubito.models import SubitoQuery

def query(query: str, url: str, install_cache: bool) -> None:

    if install_cache:
        logging.debug("Installing cache")
        requests_cache.install_cache('dubito_cache', backend="sqlite", expire_after=timedelta(hours=1))

    if query:
        subito_list_page = SubitoListPageQuery(query)
    else:
        if not validators.url(url):
            raise Exception(f'"{url}" is not a valid url, You must specify a valid url.')
        subito_list_page = SubitoListPage(url)

    # This is a transaction, if something goes wrong, the transaction is rolled back
    # In this case, the transaction also speed up the process
    subito_query = SubitoQuery(query = query)
    subito_query.save()
    with db.atomic():
        current_subito_list_page = None
        for subito_list_page_item in subito_list_page_item_iterator(subito_list_page):
            if not current_subito_list_page or current_subito_list_page != subito_list_page_item.subito_list_page:
                if current_subito_list_page:
                    print("]")
                subito_list_page_item.subito_list_page.save()
                subito_query.subito_list_pages.add(subito_list_page_item.subito_list_page)
                current_subito_list_page = subito_list_page_item.subito_list_page
                print(f"{current_subito_list_page.page_number}\t[", end='', flush=True)
            print(".", end="", flush=True)
            logging.debug(f'[bold dark_orange blink]Saving[/bold dark_orange blink] extracted Subito list page {subito_list_page_item.subito_list_page}')
            logging.debug(f'[bold dark_orange blink]Saving[/bold dark_orange blink] extracted Subito list page {subito_list_page_item}')
            subito_list_page_item.save()
        # subito_query.save()
        print()
