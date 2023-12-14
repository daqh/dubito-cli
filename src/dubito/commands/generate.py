from dubito.database import db
from dubito.subito_list_page import SubitoListPage
from dubito.models import SubitoInsertion, SubitoQuery, SubitoQuerySubitoListPageThrough
import logging

def generate():
    # Check if the database exists
    logging.info('Generating the database...')
    db.create_tables([SubitoInsertion, SubitoListPage, SubitoQuery, SubitoQuerySubitoListPageThrough])
    logging.info('Database generated.')
