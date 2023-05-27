import requests_cache
from datetime import timedelta
import logging
import argparse
from dubito.subito_list_page.iterators import subito_list_page_item_list_from_query

def main():
    parser = argparse.ArgumentParser(
        prog='dubito',
        description='Get the insertions from a query.'
    )

    parser.add_argument('query', type=str, help='The query to search.')
    parser.add_argument('--include', type=str, nargs="+", help='The query to search.', default=[])
    parser.add_argument('--exclude', type=str, nargs="+", help='The query to search.', default=[])
    parser.add_argument('--minimum-price', type=int, help='The minimum price.', default=0)
    parser.add_argument('--maximum-price', type=int, help='The maximum price.')
    parser.add_argument('--install-cache', action='store_true', help='Install the cache.', default=False)
    parser.add_argument('--verbose', action='store_true', help='Verbose.', default=False)
    args = parser.parse_args()

    query = args.query
    include = args.include
    exclude = args.exclude
    minimum_price = args.minimum_price
    maximum_price = args.maximum_price
    install_cache = args.install_cache
    verbose = args.verbose

    if verbose:
        logging.basicConfig(level=logging.INFO)

    if install_cache:
        logging.info("Installing cache")
        requests_cache.install_cache('subito_cache', backend="sqlite", expire_after=timedelta(hours=1))
    insertions = subito_list_page_item_list_from_query(query)
    print(insertions)

if __name__ == "__main__":
    main()

# insertions = pd.DataFrame(insertions)
# insertions.set_index("identifier", inplace=True)

# # # Drop duplicates
# insertions = insertions[~insertions.index.duplicated(keep='first')]

# if minimum_price:
#     insertions = insertions[insertions["price"] >= minimum_price]
# if maximum_price:
#     insertions = insertions[insertions["price"] <= maximum_price]

# q = None
# for k in include:
#     if q is None:
#         q = insertions["title"].str.contains(k, case=False)
#     else:
#         q |= insertions["title"].str.contains(k, case=False)
# if q is not None:
#     insertions = insertions[q]

# for k in exclude:
#     insertions = insertions[~insertions["title"].str.contains(k, case=False)]

# insertions.dropna(subset=["price"], inplace=True)

# q1 = insertions['price'].quantile(0.25)
# q3 = insertions['price'].quantile(0.75)
# iqr = q3 - q1
# r = 1.5
# insertions = insertions[~((insertions['price'] < (q1 - r * iqr)) | (insertions['price'] > (q3 + r * iqr)))]

# print(insertions[["title", "price"]].sort_values(by="price"))

# sns.displot(insertions, kde=True, x="price", hue="sold", multiple="stack", palette="tab10")

# plt.title(f"{query} price distribution")
# plt.show()

# # insertions[["price", "thumbnail"]].sort_values(by="price").to_csv("insertions.csv", index_label="identifier")
