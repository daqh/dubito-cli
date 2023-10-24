import argparse
from dubito.commands import query

def define_query_parser(query_parser: argparse.ArgumentParser):
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

def main():

    parser = argparse.ArgumentParser(
        prog='dubito',
        description='Get Subito insertions from a query or a url.',
        epilog='Enjoy the program! :)',
    )

    subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name', required=True)

    query_parser = define_query_parser(subparsers.add_parser('query', help='Get Subito insertions from a query or a url.'))

    args = parser.parse_args()

    if args.subparser_name == 'query':
        query(args.query, args.url, args.include, args.exclude, args.minimum_price, args.maximum_price, args.install_cache, args.verbose, args.remove_outliers)

if __name__ == "__main__":
    main()
