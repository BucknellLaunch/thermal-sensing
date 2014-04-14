from base import BaseHandler
from models import Admin

from config import app_config as cfg
from google.appengine.api import memcache

MC_LOCATIONS_KEY = cfg.get('MC_LOCATIONS_KEY', '')

def login_required(f):
	def wrapper(self, *args, **kwargs):
		if not self.admin:
			self.redirect('/login')
		else:
			f(self, *args, **kwargs)
	return wrapper

class AdminHandler(BaseHandler):
	def get_admin(self):
		aid = self.read_secure_cookie('admin_id')
		if aid:
			return Admin.by_name(aid)

class DashboardHandler(AdminHandler):
	@login_required
	def get(self):
		admin = self.get_admin()
		building = self.request.get('building')

		locations = memcache.get(MC_LOCATIONS_KEY)
		if not locations:
			locations = list(Location.all())
			memcache.set(MC_LOCATIONS_KEY, locations)

		buildings = set([location.building for location in locations])
		self.render('admin/main', admin=admin, buildings=buildings, building=building)

class AccountHandler(AdminHandler):
	@login_required
	def get(self):
		admin = self.get_admin()
		self.render('admin/account', admin=admin)