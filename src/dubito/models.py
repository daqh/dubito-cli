from dubito.subito_list_page import SubitoListPage
from peewee import *
from datetime import datetime
from dubito.base_model import BaseModel
import logging
from dubito.subito_detail_page import SubitoDetailPage, extract_and_transform_subito_detail_page

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
    condition = CharField(null=True)
    description = TextField(null=True)

    def d(self):
        subito_detail_page = SubitoDetailPage(self.url)
        logging.debug(f"Downloading {subito_detail_page}")
        extracted_and_transformed_subito_detail_page = extract_and_transform_subito_detail_page(subito_detail_page)
        self.condition = extracted_and_transformed_subito_detail_page.subito_detail_page_item["condition"]
        self.description = extracted_and_transformed_subito_detail_page.subito_detail_page_item["description"]
        return extracted_and_transformed_subito_detail_page

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title}, {self.subito_list_page.page_number})'

    class Meta:
        db_table = 'subito_insertion'

    def download():
        pass

# ------------------------------

from dubito.database import newspaper_db

class Newspaper(Model):
    '''
    A newspaper.
    
    Attributes:
    ----------
    id: int
        The id of the newspaper
    name: str
        The name of the newspaper
    '''

    id = AutoField()
    url = CharField()
    name = CharField()

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.name})'

    class Meta:
        database = newspaper_db

class NewspaperArticle(Model):
    '''
    A newspaper article.
    
    Attributes:
    ----------
    id: int
        The id of the article
    title: str
        The title of the article
    url: str
        The url of the article
    timestamp: datetime
        The timestamp of the article
    thumbnail: str
        The url of the thumbnail of the article
    newspaper: Newspaper
        The newspaper of the article
    '''

    id = AutoField()
    url = CharField()
    title = CharField(null=True)
    timestamp = DateTimeField(default=datetime.now)
    text = TextField(null=True)
    publish_date = DateTimeField(null=True)
    summary = TextField(null=True)
    newspaper = ForeignKeyField(Newspaper, backref='newspaper_articles')
    description = TextField(null=True)
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title}, {self.newspaper.name} {self.publish_date})'

    class Meta:
        database = newspaper_db
