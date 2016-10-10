
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db
from flask.ext.script import Manager, Shell

flask_app = create_app("default")

manager = Manager(flask_app)
migrate = Migrate(flask_app, db)


def make_shell_context():
    return dict(app=flask_app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()


