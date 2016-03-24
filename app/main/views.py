#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for, request
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
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=5,
        error_out=False
    )
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts, pagination=pagination)

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])

