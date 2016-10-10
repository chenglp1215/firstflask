from flask import render_template, request, url_for, jsonify
from . import vote
from .models import User


@vote.route(r'/index/', methods=["GET",])
def index():
    return render_template("vote/index.html", params={
        'redict_url': url_for("main.index")
    })


@vote.route(r'/api/index/', methods=["GET",])
def api_index():
    return jsonify([{
            'id': each.id,
            'name': each.name,
            'tel': each.tel,
            'vote': each.vote_count,
        }for each in User.query.all()])
