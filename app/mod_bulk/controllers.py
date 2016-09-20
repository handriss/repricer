from flask import Blueprint, render_template
from app import db

mod_bulk = Blueprint('bulk', __name__, url_prefix='/')


@mod_bulk.route('/', methods=['GET', 'POST'])
def signin():

    return render_template("bulk/index.html")
