from flask import Blueprint, render_template
from peewee import *
from app import db
from app.mod_xls.models import Book, BaseModel

mod_bulk = Blueprint('bulk', __name__, url_prefix='/bulk')


@mod_bulk.route('/main/', methods=['GET'])
def signin():
    books = Book.select()
    # szerző, cím, vonalkód, tárolóhely, saját ár, bookline ár, újra kell-e árazni (hidden?), két link
    titles = ['Szerző', 'Cím', 'Vonalkód', 'Tárolóhely', 'Saját ár', 'Bookline ár', 'Admin link', 'Bookline link']
    return render_template("index.html", books=books, titles=titles)
