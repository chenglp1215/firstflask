import app
from flask.ext.script import Manager

flask_app = app.app

manage = Manager(flask_app)

if __name__ == "__main__":
    manage.run()


