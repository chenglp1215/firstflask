from flask import url_for

from . import main


@main.route(r'/hello/', methods=['GET', 'POST'])
def hello():
    return "<p>hello</p><a href=%s>index</a>" % url_for('main.index')


@main.route(r'/', methods=['GET',])
def index():
    return "<p>index</p><a href=%s>hello</a>" % url_for('main.hello')


