from flask import Blueprint

from pypiorg.structure.view_mods import response
bp = Blueprint('account', __name__, template_folder='templates')

# INDEX

@bp.route('/account')
@response(template_file='account/index.html')
def index():
	return {}


# REGISTER

@bp.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
	return {}

@bp.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
	return {}


# LOGIN

@bp.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
	return {}

@bp.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
	return {}
