#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class PostForm(Form):
    head = StringField('What is your head',validators=[Required()])
    body = StringField('What is your mind', validators=[Required()])
    tag = StringField('What is post tag',validators=[Required()])
    submit = SubmitField('Submit')