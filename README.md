![Dubito Logo](assets/dubito_logo.png "Dubito")

# Dubito CLI

Dubito is a Python package that allows you to track Subito insertions. It's a simple tool that allows you to track subito insertions by specifying a query and some filters. It's useful if you want to track a specific product or if you want to track a product in a specific region or any product for a specific query.

This project was inspired by the [subito-it-searcher](https://github.com/morrolinux/subito-it-searcher) project, and its aim is to introduce notable improvements.

## Installation

To install the package you can use pip:

`pip install dubito`

Running the command:

`dubito --help`

The result will be:

```bash
usage: dubito [-h] [-l {INFO,DEBUG,WARNING,ERROR,CRITICAL}] {query,generate,find} ...

Get Subito insertions from a query or a url.

positional arguments:
  {query,generate,find}
                        sub-command help
    query               Get Subito insertions from a query or a url.
    generate            Generate a Dubito project.
    find                Find a query in the database.

options:
  -h, --help            show this help message and exit
  -l {INFO,DEBUG,WARNING,ERROR,CRITICAL}, --log-level {INFO,DEBUG,WARNING,ERROR,CRITICAL}
                        Log level.

Enjoy the program! :)
```

## Data Extrapolation

```bash
usage: dubito query [-h] (-q QUERY | --url URL) [--install-cache]

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        The query to search.
  --url URL             The url to search.
  --install-cache       Install the cache.
```

# Data selection

```bash
usage: dubito find [-h] query

positional arguments:
  query       The query to search.

options:
  -h, --help  show this help message and exit
```

Where `query` is an SQL query used to select the data:

`dubito find "select s.id, s.title, s.price from subito_insertion as s where s.title like '%iphone 12 mini%' and s.price > 100 order by s.price" > result.csv`

# Data visualization

Coming soon...
