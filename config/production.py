import os

from config.common import Config, basedir


class FullConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-pro.sqlite')
