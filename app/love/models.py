# coding=utf-8

from app import db


class EachDayText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    create_time = db.Column(db.DateTime)
    show_counts = db.Column(db.Integer, default=0)
    confs = db.relationship('EachDayConf', backref='text')

    __tablename__ = 'each_day_text'
    __tableplay__ = u'每日一句'

    def __str__(self):
        return u'%s: %s' % (self.id, self.text)

    def __repr__(self):
        return u'<EachDayText: %s>' % self.id


class EachDayMusic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_title = db.Column(db.String(20))
    music_url = db.Column(db.String(200))
    create_time = db.Column(db.DateTime)
    show_counts = db.Column(db.Integer, default=0)
    confs = db.relationship('EachDayConf', backref='music')

    __tablename__ = 'each_day_music'
    __tableplay__ = u'每日一歌'

    def __str__(self):
        return u'%d' % self.id

    def __repr__(self):
        return u'<EachDayMusic: %s>' % self.id


class EachDayArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    article = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    show_counts = db.Column(db.Integer, default=0)
    confs = db.relationship('EachDayConf', backref='article')

    __tablename__ = 'each_day_article'
    __tableplay__ = u'每日一文'

    def __str__(self):
        return u'%s: %s' % (self.id, self.title)

    def __repr__(self):
        return u'<EachDayArticle: %s>' % self.id


class EachDayConf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_id = db.Column(db.Integer, db.ForeignKey("each_day_text.id"))
    music_id = db.Column(db.Integer, db.ForeignKey("each_day_music.id"))
    article_id = db.Column(db.Integer, db.ForeignKey("each_day_article.id"))
    date = db.Column(db.Date)

    __tablename__ = 'each_day_conf'
    __tableplay__ = u'每日配置'

    def __str__(self):
        return u'%d: %s' % (self.id, self.date.strftime('%Y-%m-%d'))

    def __repr__(self):
        return u'<EachDayConf: %s>' % self.id
