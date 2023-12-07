from dubito.subito_list_page import SubitoListPage
from dubito.database import db
from peewee import *

class SubitoInsertion(Model):

    id = AutoField()
    title = CharField()
    url = CharField()
    subito_list_page = ForeignKeyField(SubitoListPage, backref='subito_insertions')

    def __str__(self):

        return f'{self.id} - {self.title}'
    
    class Meta:
        database = db

db.create_tables([SubitoInsertion])
