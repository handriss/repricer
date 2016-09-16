from peewee import *
import sqlite3
from app import db


class BaseModel(Model):

    class Meta:
        database = db


class Book(BaseModel):
    status = CharField()
    description_id = IntegerField()
    book_id = IntegerField()
    author = CharField()
    title = CharField()
    publication_year = IntegerField()
    publisher = CharField()
    code = IntegerField()
    storage_place = CharField()
    picture_url = CharField()
    price = IntegerField()
    uploaded = DateTimeField()
    sold_in_shop = DateTimeField()
    shop = IntegerField()
    weight = FloatField()
    number_of_pages = IntegerField()
    cover = CharField()
    quality = CharField()
    moreinfo = TextField()
    uploader = CharField()
    category = CharField()
    annotation = TextField()
    publication_id = IntegerField()
    isbn = IntegerField()
