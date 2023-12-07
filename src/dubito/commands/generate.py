from dubito.database import db
from dubito.subito_list_page import SubitoListPage
from dubito.models import SubitoInsertion

def generate():
    db.create_tables([SubitoInsertion, SubitoListPage])
