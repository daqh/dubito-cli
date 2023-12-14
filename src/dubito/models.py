from dubito.subito_list_page import SubitoListPage
from peewee import *
from datetime import datetime
from dubito.base_model import BaseModel

class SubitoQuery(BaseModel):
    '''
    A collection of Subito list pages.
    
    Attributes:
    ----------
    id: int
        The id of the collection
    name: str
        The name of the collection
    '''

    id = AutoField()
    timestamp = DateTimeField(default=datetime.now)
    query = CharField()
    subito_list_pages = ManyToManyField(SubitoListPage)

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.query})'

    class Meta:
        db_table = 'subito_query'

class SubitoQuerySubitoListPageThrough(BaseModel):
    '''
    A Subito list page through model.
    
    Attributes:
    ----------
    id: int
        The id of the model
    subito_list_page: SubitoListPage
        The subito list page
    subito_query: SubitoQuery
        The subito query
    '''

    id = AutoField()
    subitolistpage_id = ForeignKeyField(SubitoListPage, backref='subito_list_pages')
    subitoquery_id = ForeignKeyField(SubitoQuery, backref='subito_queries')

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.subito_list_page.page_number}, {self.subito_query.query})'

    class Meta:
        db_table = 'subito_query_subito_list_page_through'

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
    created_at: datetime
        The creation date of the insertion
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
    created_at = DateTimeField(null=True)
    price = FloatField(null=True)
    sold = BooleanField()
    shipping_available = BooleanField()
    subito_list_page = ForeignKeyField(SubitoListPage, backref='subito_insertions')

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title}, {self.subito_list_page.page_number})'

    class Meta:
        db_table = 'subito_insertion'

    def download():
        pass
