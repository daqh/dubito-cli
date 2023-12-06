import argparse
from dubito.commands import query

def define_query_parser(query_parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    query_or_url_group = query_parser.add_mutually_exclusive_group(required=True)
    query_or_url_group.add_argument('-q', '--query', type=str, help='The query to search.')
    query_or_url_group.add_argument('--url', type=str, help='The url to search.')
    query_parser.add_argument('-i', '--include', type=str, nargs="+", help='Exclude keywords from the query to search.', default=[])
    query_parser.add_argument('-e', '--exclude', type=str, nargs="+", help='Include keywords from the query to search.', default=[])
    query_parser.add_argument('--minimum-price', type=int, help='The minimum price.')
    query_parser.add_argument('--maximum-price', type=int, help='The maximum price.')
    query_parser.add_argument('--install-cache', action='store_true', help='Install the cache.', default=False)
    query_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose.', default=False)
    query_parser.add_argument('--remove-outliers', action='store_true', help='Remove outliers.', default=False)
    return query_parser

from subito_list_page import SubitoListPage

def main():
    subito_list_page = SubitoListPage(url="https://subito.it?q=macbzook")
    print(subito_list_page)
    subito_list_page.save()
    print(subito_list_page)
    subito_list_page = subito_list_page[2]
    print(subito_list_page)
    subito_list_page.save()
    print(subito_list_page)

if __name__ == "__main__":
    main()
