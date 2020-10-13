import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = True  # Turns on debugging features in Flask
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'pypiorg/db/app.sqlite')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
