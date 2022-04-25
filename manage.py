import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import secrets
from app import create_app, db
from app.models import setup
from main import blueprint


app = create_app(os.environ['APP_SETTINGS'])
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def generate_api_key():
    key = secrets.token_hex(32)
    new_key = setup.Setup(
        api_key=key,
    )
    db.session.add(new_key)
    db.session.commit()
    return "new api-key generated: " + str(key)


if __name__ == '__main__':
    manager.run()