
import requests

class Insertion:

    def __init__(self, title, price, thumbnail, link, city, state, time, description):
        self.title = title
        self.price = price
        self.thumbnail = thumbnail
        self.link = link
        self.city = city
        self.state = state
        self.time = time
        self.description = description

    def load(self):
        response = requests.get(self.link)
    