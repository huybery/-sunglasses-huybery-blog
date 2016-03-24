#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from flask.ext.login import login_required

from . import main
from .forms import PostForm
from .. import db
from ..models import Post,Item
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@main.route('/', methods=['GET','POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        tag = Item(tag=form.tag.data)
        post = Post(body=form.body.data, head=form.head.data, item=tag)
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

@main.route('/edit/<int:id>',methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.head = form.head.data
        post.body = form.body.data
        post.item.tag = form.tag.data
        db.session.add(post)
        db.session.commit()
        flash('文章修改完成！(`･ω･´)ゞ ')
        return redirect(url_for('.post', id=post.id))
    form.body.data = post.body
    form.head.data = post.head
    form.tag.data = post.item.tag
    return render_template('edit_post.html', form=form)

@main.route('/item/<tag>',methods=['GET','POST'])
def item(tag):
    vector=[]
    items=Item.query.filter_by(tag=tag).all()
    for item in items:
        vector.append(item.posts[0])
    posts = vector
    posts.reverse()
    return render_template('item.html', posts=posts)

