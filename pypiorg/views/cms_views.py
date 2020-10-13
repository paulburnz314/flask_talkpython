from flask import Blueprint

from pypiorg.structure.view_mods import response
import pypiorg.services.cms_service as cms_service

bp = Blueprint('cms', __name__, template_folder='templates')


@bp.route('/<path:full_url>')
@bp.route('/index')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
	print(f"Getting CMS page for {full_url}.")

	page = cms_service.get_page(full_url)
	if not page:
		flask.abort(404)

	return page

