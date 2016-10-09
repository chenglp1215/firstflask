from app import app
from flask.ext.script import Manager

manage = Manager(app)

if __name__ == "__main__":
    manage.run()


