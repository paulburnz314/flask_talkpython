from flask import Blueprint

from pypiorg.structure.view_mods import response
# import app.services.package_service as package_service

bp = Blueprint('packages', __name__, template_folder='templates')


@bp.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
	# test_packages = package_service.get_latest_packages()
	return {f'Package details for {package_name}'}


@bp.route('/<int:rank>')
def popular(rank: int):
	print(type(rank), rank)
	return f"The details for the {rank}th most popular package"
