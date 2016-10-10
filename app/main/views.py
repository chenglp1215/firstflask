from flask import url_for, render_template, request

from . import main


@main.route(r'/hello/', methods=['GET', 'POST'])
def hello():
    return render_template('hello.html', params={
        'redict_url': request.referrer or url_for('main.index')
    })


@main.route(r'/', methods=['GET',])
def index():
    return render_template('index.html', params={
        'redict_url': url_for('main.hello')
    })


@main.route(r'/wx', methods=['GET',])
def wx_token():
    with open('wxlog.log', 'a') as logfile:
        logfile.write('%s\n' % str(request.args))
    return "test"