from peewee import *
import sqlite3
from app import db


class BaseModel(Model):
    """A base model that will use our sqlite database"""

    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    password = CharField()
