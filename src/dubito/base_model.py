from peewee import *
from dubito.database import dubito_db

class BaseModel(Model):

    class Meta:
        database = dubito_db
