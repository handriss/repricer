from flask import Blueprint, render_template
from peewee import *
from app import db
from app.mod_xls.models import Book, BaseModel

mod_bulk = Blueprint('bulk', __name__, url_prefix='/bulk')


@mod_bulk.route('/main/', methods=['GET'])
def signin():
    print("mukodj")
    books = Book.select()
    my_list = [1, 3, 235, 4]
    for book in books:
        print(book.author)
    return render_template("header_footer.html", books=my_list)
