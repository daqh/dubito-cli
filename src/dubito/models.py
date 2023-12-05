from peewee import *

db = SqliteDatabase('database.sqlite')

class SubitoListPage(Model):
    
        id = PrimaryKeyField()
        url = CharField()
        query = CharField(null=True)

        class Meta:
            database = db

class SubitoInsertion(Model):

    id = PrimaryKeyField()
    title = CharField()
    url = CharField()
    thumbnail = CharField(null=True)
    price = FloatField(null=True)
    description = CharField(null=True)
    city = CharField(null=True)
    state = CharField(null=True)
    subito_list_page = ForeignKeyField(SubitoListPage, backref='subito_insertions', on_delete='CASCADE')

    class Meta:
        database = db

db.create_tables([SubitoInsertion, SubitoListPage])
db.close()
