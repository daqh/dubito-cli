# Dubito

Dubito is a Python package that allows you to track Subito ads. It's a simple tool that allows you to track ads by specifying a query and some filters. It's useful if you want to track a specific product or if you want to track a product in a specific region.

## Example usage of the CLI

This will download the first page of the query `gtx 1070` and save the data in a CSV file.

`dubito "gtx 1070" --install-cache  -i 1070 -e pc i7 ryzen --minimum-price 90 --remove-outliers > out.csv`

This will download the first page of the query `gtx 1070` and save the data in a JSON file.

`dubito "gtx 1070" --install-cache  -i 1070 -e pc i7 ryzen --minimum-price 90 --remove-outliers -o json > out.json`

