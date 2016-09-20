from peewee import *
import sqlite3
from app import db


class BaseModel(Model):

    class Meta:
        database = db


class Book(BaseModel):
    status = CharField()
    description_id = CharField()
    book_id = CharField()
    author = CharField()
    title = CharField()
    publication_year = CharField()
    publisher = CharField()
    barcode = CharField()
    storage_place = CharField()
    picture_url = CharField()
    price = CharField()
    uploaded = DateTimeField()
    sold_in_shop = DateTimeField()
    shop = CharField()
    weight = FloatField()
    number_of_pages = CharField()
    cover = CharField()
    quality = CharField()
    moreinfo = TextField()
    uploader = CharField()
    category = CharField()
    annotation = TextField()
    publication_id = CharField()
    isbn = CharField()

    bookline_price = CharField(null=True)
    admin_link = CharField(null=True)
    bookline_Link = CharField(null=True)
