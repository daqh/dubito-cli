# Dubito

Dubito is a Python package that allows you to track Subito ads. It's a simple tool that allows you to track ads by specifying a query and some filters. It's useful if you want to track a specific product or if you want to track a product in a specific region.

## Example usage

`python3 -m subito_tracker --query "gtx 1070" --include 1070 --exclude pc ryzen i7 --minimum-price 100 --install-cache`

## Project structure

### The pipeline of `SubitoPageList`

The pipeline is the core of the project. It's a three step process in which we build a list page, extract the data from the list page and transform the data.

1. [Build a list page](#1-build-a-list-page)

    1.1. [Build a list page from a URL](#11-build-a-list-page-from-a-url)

    1.2 [Build a list page from a query](#12-build-a-list-page-from-a-query)

2. [Extract data of a list page](#2-extract-data-of-a-list-page)

    2.1 [Extract data specifying the query](#21-extract-data-specifying-the-query)

    2.2 [Extract data from a list page object](#22-extract-data-from-a-list-page-object)

3. [Transform data of a list page](#3-transform-data-of-a-list-page)

    3.1 [Transform data specifying the query](#31-transform-data-specifying-the-query)

    3.2 [Transform data from an extracted list page object](#32-transform-data-from-an-extracted-list-page-object)


---

#### 1 Build a list page

This is the first step of the pipeline. You can build a list page from a URL or from a query. This object simply describes the list page, it doesn't download the page data. It's useful if you want to download the page data later.

##### 1.1 Build a list page from a URL

```python
from dubito.subito_list_page import SubitoListPage

list_page = SubitoListPage("https://www.subito.it/annunci-italia/vendita/usato/?q=gtx+1070")
```

##### 1.2 Build a list page from a query

Cons of this method is that you can't specify the region.

```python
from dubito.subito_list_page import SubitoQueryListPage

list_page = SubitoQueryListPage("gtx 1070")
print(list_page.url)            # https://www.subito.it/annunci-italia/vendita/usato/?q=gtx+1070

print(list_page.query)          # gtx 1070

print(list_page.page_number)    # 1
```

---

Once we have a list page, we can download the page data by simply instantiating the `ExtractedSubitoListPage` class.

#### 2 Extract data of a list page

In the second step of the pipeline we extract the data from the list page. The extraction activity is the activity in which we perform an HTTP request to download the page data. This is the most expensive step of the pipeline in terms of time and resources.

##### 2.1 Extract data specifying the query

Using the `ExtractedSubitoListPage` methods is the easiest way to extract data from a list page. It allows you to specify the query or the entire url.

```python
# Specify the query (cons: you can't specify the region)
from dubito.subito_list_page import ExtractedSubitoListPage

# You can specify the page number (default is 1)
extracted_list_page = ExtractedSubitoListPage.from_query("gtx 1070", 3)
```

```python
# Specifiy the url  (pros: you can specify the region)
from dubito.subito_list_page import ExtractedSubitoListPage

extracted_list_page = ExtractedSubitoListPage.from_url("https://www.subito.it/annunci-italia/vendita/usato/?q=gtx+1070")
```

##### 2.2 Extract data from a list page object

Another way to extract data from a list page is to build it directly from a `SubitoListPage` object. This is useful if you want to download a list page that you already know.

```python
from dubito.subito_list_page import ExtractedSubitoListPage, SubitoQueryListPage

list_page = SubitoQueryListPage("gtx 1070")
extracted_list_page = ExtractedSubitoListPage(list_page)
```

---

#### 3 Transform data of a list page

In the third and last step, we transform the data obtained from the list page. This is the step in which we parse the HTML and extract the data.

##### 3.1 Transform data specifying the query

As for the extraction, the easiest way to transform the data is to use the `TransformedSubitoListPage` methods. It allows you to specify the query or the entire url. 

```python
# Specify the query
from dubito.subito_list_page import TransformedSubitoListPage

transformed_list_page = TransformedSubitoListPage.from_query("gtx 1070", 22)
```

```python
# Specifiy the url
from dubito.subito_list_page import TransformedSubitoListPage

transformed_list_page = TransformedSubitoListPage.from_url("https://www.subito.it/annunci-italia/vendita/usato/?q=gtx+1070")
```

##### 3.2 Transform data from an extracted list page object

Another way to transform data from a list page is to build it directly from an `ExtractedSubitoListPage` object. This is useful if you want to transform a list page that you've already downloaded.

```python
from dubito.subito_list_page import TransformedSubitoListPage, ExtractedSubitoListPage

extracted_list_page = ExtractedSubitoListPage.from_query("gtx 1070", 3)
transformed_list_page = TransformedSubitoListPage(extracted_list_page)
```
