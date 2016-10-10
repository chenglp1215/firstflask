import os

from config.common import Config, basedir


class FullConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-default.sqlite')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True