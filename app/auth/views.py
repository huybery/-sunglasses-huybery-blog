#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import redirect, request, url_for, flash, render_template
from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('main.index'))