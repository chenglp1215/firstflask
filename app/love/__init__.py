from flask import Blueprint

love = Blueprint("love", __name__)

from . import views, errors, models, admin

