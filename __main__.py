from tkinter import INSERT
from insertion import Insertion
from selectorlib import Extractor
import requests
import json
from time import sleep

insertions_extractor = Extractor.from_yaml_file('insertions.yaml')
insertion_extractor = Extractor.from_yaml_file('insertion.yaml')

def get_search_result(query: str, page: int = 1):
    url = "https://www.subito.it/annunci-italia/vendita/usato/?q={query}&order=datedesc&o={page}".format(query=query, page=page)
    insertions_response = requests.get(url)
    if(insertions_response.status_code >= 500):
        raise Exception("Error {response.status_code}")
    if(insertions_response.status_code >= 400):
        raise Exception("Error {response.status_code}")
    else:
        insertions_data = insertions_extractor.extract(insertions_response.text)
        insertions = []
        for i in insertions_data["insertions"]:
            title = i["title"]
            link = i["link"]
            insertion_response = requests.get(link)
            insertion_data = insertion_extractor.extract(insertion_response.text)
            price = insertion_data["price"]
            description = insertion_data["description"]
            insertions.append(Insertion(title, price, i["thumbnail"], i["link"], i["city"], i["state"], i["time"], description))
        return insertions

insertions = get_search_result("MacBook+Air+M1")

for i in insertions:
    print(i.title, i.price)
