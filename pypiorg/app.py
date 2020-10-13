import os
import sys
from flask import Flask
# import app.data.__all_models
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from app.config import Config
# abspath returns absolute path of a path
# join means join to path strings
# dirname returns the directory of a file
# __file__ refers to the script's file name
# pardir is represented by ..
# below most likely equals the \flask-talkpython directory
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, basedir)

import pypiorg.data.db_session as db_session
# db = SQLAlchemy()
# migrate = Migrate()
app = Flask(__name__)


def main():
	# app.config.from_object(config_class)
	# db.init_app(app)
	# migrate.init_app(app, db)
	register_blueprints()
	setup_db()
	app.run(debug=True)
	return basedir
	# print(f'Connecting to database with {config_class.SQLALCHEMY_DATABASE_URI}')


def setup_db():
	db_file = os.path.join(os.path.dirname(__file__), 'db', 'app.sqlite')
	db_session.global_init(db_file)


def register_blueprints():
	from pypiorg.views.home_views import bp as home_bp
	app.register_blueprint(home_bp)

	from pypiorg.views.package_views import bp as package_bp
	app.register_blueprint(package_bp)

	from pypiorg.views.cms_views import bp as cms_bp
	app.register_blueprint(cms_bp)

	from pypiorg.views.account_views import bp as account_bp
	app.register_blueprint(account_bp)


if __name__ == '__main__':
	main()
