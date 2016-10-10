# coding=utf-8
from app import db


class User(db.Model):
    __tablename__ = 'vote_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(32), index=True)
    tel = db.Column(db.String(32), nullable=True)
    intro = db.Column(db.String(256), nullable=True)
    sex = db.Column(db.Boolean, nullable=True)
    vote_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __str__(self):
        return u'%d:%s' % (self.id, self.name)

    def __repr__(self):
        return u'<User: %s>' % self.name

