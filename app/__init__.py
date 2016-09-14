# Import flask and template operators
from flask import Flask, render_template
import sqlite3
from peewee import *

db = SqliteDatabase('users.db')

from app.mod_auth.models import *

users = [{"name": "admin", "password": "admin"}, {"name": "admin2", "password": "admin2"}]
db.connect()
db.drop_tables([User], safe=True)
db.create_tables([User], safe=True)


with db.atomic():
    User.insert_many(users).execute()

app = Flask(__name__)
app.config.from_object('config')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_auth.controllers import mod_auth as auth_module

app.register_blueprint(auth_module)

users = [{"name": "admin", "password": "admin"}, {"name": "admin2", "password": "admin2"}]
db.connect()
db.drop_tables([User], safe=True)
db.create_tables([User], safe=True)


with db.atomic():
    User.insert_many(users).execute()
