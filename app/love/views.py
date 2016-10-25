from flask import render_template, request, url_for, jsonify, session

from app.love import love
from .models import EachDayText, EachDayArticle
from app import babel


@love.route(r'/api/index/', methods=["GET",])
def api_index():
    return jsonify([{
            'id': each.id,
            'text': each.text,
        }for each in EachDayText.query.all()])


@love.route(r'/',methods=['GET'])
def index():
    return "hello"


@love.route(r'/article/<article_id>', methods=['GET'])
def article_info(article_id):
    article = EachDayArticle.query.filter_by(id=article_id).first()
    return jsonify({
        'id': article.id,
        'title': article.title,
        'article': article.article
    })

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'en')