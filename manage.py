#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.models import User,Role,Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app)
manager.add_command("shell",Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()