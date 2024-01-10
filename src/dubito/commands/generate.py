from dubito.database import dubito_db
from dubito.subito_list_page import SubitoListPage
from dubito.models import SubitoInsertion, SubitoQuery, SubitoQuerySubitoListPageThrough
from dubito.models import Newspaper, NewspaperArticle
import logging

def generate():
    # Check if the database exists
    logging.info('Generating the database...')
    dubito_db.create_tables([SubitoInsertion, SubitoListPage, SubitoQuery, SubitoQuerySubitoListPageThrough])
    dubito_db.create_tables([Newspaper, NewspaperArticle])
    logging.info('Database generated.')
