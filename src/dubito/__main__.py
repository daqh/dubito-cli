import requests_cache
from datetime import timedelta
import logging
import argparse
import pandas as pd
import validators
from dubito.subito_list_page import SubitoListPage, SubitoListPageQuery, subito_list_page_item_iterator
from rich.logging import RichHandler
from rich.console import Console

def main():

    parser = argparse.ArgumentParser(
        prog='dubito',
        description='Get Subito insertions from a query or a url.',
        epilog='Enjoy the program! :)',
    )

    query_or_url_group = parser.add_mutually_exclusive_group(required=True)
    query_or_url_group.add_argument('-q', '--query', type=str, help='The query to search.')
    query_or_url_group.add_argument('--url', type=str, help='The url to search.')
    parser.add_argument('-i', '--include', type=str, nargs="+", help='Exclude keywords from the query to search.', default=[])
    parser.add_argument('-e', '--exclude', type=str, nargs="+", help='Include keywords from the query to search.', default=[])
    parser.add_argument('--minimum-price', type=int, help='The minimum price.')
    parser.add_argument('--maximum-price', type=int, help='The maximum price.')
    parser.add_argument('--install-cache', action='store_true', help='Install the cache.', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose.', default=False)
    parser.add_argument('-o', '--output', type=str, help='The output file.', default="csv")
    parser.add_argument('--remove-outliers', action='store_true', help='Remove outliers.', default=False)
    args = parser.parse_args()

    query = args.query
    url = args.url
    include = args.include
    exclude = args.exclude
    minimum_price = args.minimum_price
    maximum_price = args.maximum_price
    install_cache = args.install_cache
    verbose = args.verbose
    remove_outliers = args.remove_outliers

    if verbose:
        import sys
        console = Console(file=sys.stderr)
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[RichHandler(console=console, markup=True)],
        )

    if install_cache:
        logging.info("Installing cache")
        requests_cache.install_cache('dubito_cache', backend="sqlite", expire_after=timedelta(hours=1))

    if query:
        subito_list_page_items = list(subito_list_page_item_iterator(SubitoListPageQuery(query)))
    else:
        if not validators.url(url):
            raise Exception(f'"{url}" is not a valid url, You must specify a valid url.')
        subito_list_page_items = list(subito_list_page_item_iterator(SubitoListPage(url)))

    # Convert the downloaded items to a pandas dataframe and applies some filters

    df = pd.DataFrame(subito_list_page_items).set_index("identifier")
    df = df[~df.index.duplicated(keep='first')]

    # Filer 1: Get everything under the specified price
    if minimum_price is not None:
        df = df[df["price"] >= minimum_price]

    # Filer 2: Get everything over the specified price
    if maximum_price is not None:
        df = df[df["price"] <= maximum_price]

    # Filer 3: Get everything that contains the specified keywords
    q = None
    for k in include:
        if q is None:
            q = df["title"].str.contains(k, case=False)
        else:
            q |= df["title"].str.contains(k, case=False)
    if q is not None:
        df = df[q]

    # Filer 4: Get everything that does not contain the specified keywords
    for k in exclude:
        df = df[~df["title"].str.contains(k, case=False)]

    # Filer 5: Remove outliers
    if remove_outliers:
        q1 = df['price'].quantile(0.25)
        q3 = df['price'].quantile(0.75)
        iqr = q3 - q1
        r = 1.5
        df = df[~((df['price'] < (q1 - r * iqr)) | (df['price'] > (q3 + r * iqr)))]

    # Finally, sort by price
    df = df.sort_values(by=["price"])

    if args.output == "csv":
        print(df.to_csv())
    elif args.output == "json":
        print(df.transpose().to_json(indent=4))
    else:
        raise Exception("Invalid output format")

if __name__ == "__main__":
    main()
