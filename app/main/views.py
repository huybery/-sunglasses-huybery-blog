#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask import  render_template,session,redirect,url_for
from flask.ext.login import login_required

from . import main
from .forms import PostForm
from .. import db
from ..models import Post

@main.route('/', methods=['GET','POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data,head=form.head.data,tag=form.tag.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])

