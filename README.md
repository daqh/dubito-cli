# Dubito

Dubito is a Python package that allows you to track Subito insertions. It's a simple tool that allows you to track subito insertions by specifying a query and some filters. It's useful if you want to track a specific product or if you want to track a product in a specific region or any product for a specific query.

## Installation

To install the package you can use pip:

`pip install dubito`

## Example usage of the CLI

This will download and transform the first page of the query `gtx 1070` and save the data in a CSV file.

`dubito --query "gtx 1070" --install-cache  -i 1070 -e pc i7 ryzen --minimum-price 90 --remove-outliers > out.csv`

This will download and transform the first page of the query `gtx 1070` and save the data in a JSON file.

`dubito -q "gtx 1070" --install-cache  -i 1070 -e pc i7 ryzen --minimum-price 90 --remove-outliers -o json > out.json`

## Iterate over the items every list page of a query

If you want to iterate over the items of every list page of a query you can use the `subito_list_page_item_iterator` function. This function takes a `SubitoListPage` object as input and returns a generator that yields the items of every list page of the query. The iterator will stop when finds a page with no items.

```python
from dubito.subito_list_page import subito_list_page_item_iterator, SubitoListPageQuery

for item in subito_list_page_item_iterator(SubitoListPageQuery("nintendo switch")):
    print(item["title"], item["price"])
```

## Iterate over list pages of a query

The iterator will stop when finds a page with no items.

```python
from dubito.subito_list_page import extract_and_transform_subito_list_page, SubitoListPage

for list_page in extract_and_transform_subito_list_page(SubitoListPage("https://www.subito.it/annunci-italia/vendita/usato/?q=nintendo%20switch")):
    print(len(list_page.items))
```

