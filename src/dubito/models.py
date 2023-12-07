from dubito.subito_list_page import SubitoListPage
from peewee import *
from datetime import datetime

from dubito.base_model import BaseModel

class SubitoInsertion(BaseModel):
    '''
    A Subito insertion.
    
    Attributes:
    ----------
    id: int
        The id of the insertion
    title: str
        The title of the insertion
    url: str
        The url of the insertion
    timestamp: datetime
        The timestamp of the insertion
    thumbnail: str
        The url of the thumbnail of the insertion
    city: str
        The city of the insertion
    state: str
        The state of the insertion
    price: float
        The price of the insertion
    sold: bool
        Whether the insertion is sold or not
    subito_list_page: SubitoListPage
        The subito list page of the insertion
    '''

    id = AutoField()
    title = CharField()
    url = CharField()
    timestamp = DateTimeField(default=datetime.now)
    thumbnail = CharField()
    city = CharField(null=True)
    state = CharField(null=True)
    # TODO: Add time field
    price = FloatField(null=True)
    sold = BooleanField()
    subito_list_page = ForeignKeyField(SubitoListPage, backref='subito_insertions')

    def __str__(self):

        return f'{self.__class__.__name__}({self.id}, {self.title}, {self.subito_list_page.page_number})'
