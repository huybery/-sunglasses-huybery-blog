#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length

class LoginForm(Form):
    name = StringField('name',validators=[Required()])
    passwrod = PasswordField('password',validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')