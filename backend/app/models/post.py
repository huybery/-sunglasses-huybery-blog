"""
model for post
"""

from app import blog
from app import db

class Post(db.Document):
    """
    文章 model 层
    """
    title = db.StringField(require=True)
    body = db.StringField(require=True)
    # tag = db.StringField()
    views = db.IntField(require=True)


    def add_views(self, init=False):
        if init:
            self.views = 0
        else:
            self.views += 1