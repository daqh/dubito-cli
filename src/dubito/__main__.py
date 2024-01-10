import argparse
from dubito.commands import query, generate, find, analyze, fetch
from rich.logging import RichHandler
import logging

def define_query_parser(query_parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    query_or_url_group = query_parser.add_mutually_exclusive_group(required=True)
    query_or_url_group.add_argument('-q', '--query', type=str, help='The query to search.')
    query_or_url_group.add_argument('--url', type=str, help='The url to search.')
    query_parser.add_argument('--install-cache', action='store_true', help='Install the cache.', default=False)
    return query_parser

def define_find_parser(find_parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    find_parser.add_argument('query', type=str, help='The query to search.')
    return find_parser

def define_analyze_parser(analyze_parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    analyze_parser.add_argument('keywords', type=str, nargs='+', help='The keywords to analyze.')
    return analyze_parser

def define_fetch_parser(fetch_parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    fetch_parser.add_argument('url', type=str, help='The url to search.')
    fetch_parser.add_argument('--language', type=str, help='The language of the url.', default='it')
    return fetch_parser

def main():
    parser = argparse.ArgumentParser(
        prog='dubito',
        description='Get Subito insertions from a query or a url.',
        epilog='Enjoy the program! :)',
    )
    parser.add_argument('-l', '--log-level', type=str, choices=['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'], help='Log level.', default='INFO')

    subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name', required=True)

    query_parser = define_query_parser(subparsers.add_parser('query', help='Get Subito insertions from a query or a url.'))
    generate_parser = subparsers.add_parser('generate', help='Generate a Dubito project.')
    find_parser = define_find_parser(subparsers.add_parser('find', help='Find a query in the database.'))
    analyze_parser = define_analyze_parser(subparsers.add_parser('analyze', help='Analyze a query.'))
    fetch_parser = define_fetch_parser(subparsers.add_parser('fetch', help='Fetch a newspaper.'))

    args = parser.parse_args()

    log_level = args.log_level

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        handlers=[RichHandler(markup=True)],
    )

    if args.subparser_name == 'query':
        query(args.query, args.url, args.install_cache)
    elif args.subparser_name == 'generate':
        generate()
    elif args.subparser_name == 'find':
        find(args.query)
    elif args.subparser_name == 'analyze':
        analyze(args.keywords)
    elif args.subparser_name == 'fetch':
        fetch(args.url, args.language)

if __name__ == "__main__":
    main()
