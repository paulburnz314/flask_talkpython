from flask import Blueprint

from pypiorg.structure.view_mods import response
import pypiorg.services.package_service as package_service

bp = Blueprint('home', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/index')
@response(template_file='home/index.html')
def index():
	test_packages = package_service.get_latest_packages()
	return {'packages': test_packages}


@bp.route('/about')
@response(template_file='home/about.html')
def about():
	return {}


@bp.route('/hello')
def hello():
	return 'Hello, World!'
