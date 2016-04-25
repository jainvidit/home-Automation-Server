import logging
import os.path
import sys

from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from home_automation.models import db
from home_automation.models.user import User
from home_automation.models.location import Location
from home_automation.views.model_views.user import UserView
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app():
    print("app init")
    app = Flask(__name__)
    from home_automation.views import app as routes
    app.register_blueprint(routes)
    Migrate(app, db)

    db.init_app(app)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://my_user:marullz..@localhost:5432/test"
    admin = Admin(app, name='Home Automation', template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Location, db.session))
    return app, manager, db


current_app, manager, database = create_app()
