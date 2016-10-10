# coding=utf-8
from flask import url_for, render_template, request, current_app

from . import main
import hashlib


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

    signature = request.args.get('signature')
    token = current_app.config.get("WX_TOKEN")
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    temarr = [timestamp, nonce, token]
    tmpstr = hashlib.sha1(''.join(temarr)).hexdigest()
    with open(current_app.config.get('WX_LOG_FILE'), 'a') as logfile:
        logfile.write('GET: sign->%s, timestamp->%s, nonce->%s echostr->%s\n' % (signature, timestamp, nonce, echostr))
        logfile.write('MYSIGN: sign->%s\n' % tmpstr)
    if tmpstr == signature:
        # 认证成功
        return echostr
    else:
        return "error"
