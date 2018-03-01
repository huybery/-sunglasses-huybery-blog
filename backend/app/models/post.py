"""
model for post
"""

from app import blog
from app import db
import datetime

class Post(db.Document):
    """
    文章 model 层
    """
    title = db.StringField(require=True)
    body = db.StringField(require=True)
    mark = db.StringField(require=True)
    # tag = db.StringField()
    views = db.IntField(require=True)
    timestamp = db.DateTimeField(require=True, default=datetime.datetime.now())

    def get_dict(self):
        new_post = {
            'task' : {
                'title': self.title,
                'body': self.body,
                'views': self.views, 
                'mark': self.mark,
                'timestamp': self.timestamp.strftime("%Y-%m-%d")
        }}
        return new_post

    def add_views(self, init=False):
        if init:
            self.views = 0
        else:
            self.views += 1
