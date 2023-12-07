from peewee import *
from dubito.database import db

class BaseModel(Model):

    class Meta:
        database = db
