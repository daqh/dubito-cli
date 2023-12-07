from dubito.subito_list_page import SubitoListPage
from dubito.database import db
from peewee import *
from datetime import datetime

class SubitoInsertion(Model):

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

        return f'{self.id} - {self.title}'
    
    class Meta:
        database = db

db.create_tables([SubitoInsertion])
