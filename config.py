#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'meiyoushezhimima'
    SQLALCHEMY_COMMIT_ON_REARDOWN = True
    SQLALCHEMY_DATABASE_URI=''
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass