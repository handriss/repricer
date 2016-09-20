from flask import Blueprint, render_template
from app import db

mod_bulk = Blueprint('bulk', __name__, url_prefix='/bulk')


@mod_bulk.route('/main/', methods=['GET'])
def signin():
    return render_template("index.html")
