from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo
from peewee import *
from app.mod_auth.models import Visitor
import wtforms



class LoginForm(Form):
    # email = wtforms.TextField('Email Address')
    # password = PasswordField('Password', [Required(message='Must provide a password. ;-)')])

    name = wtforms.TextField('Email Address')
    password = PasswordField('Password')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = Visitor.get(name=self.name.data)
        if user is None:
            self.name.errors.append('Unknown username')
            return False

        if user.password != self.password.data:
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
