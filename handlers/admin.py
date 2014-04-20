import json
from base import BaseHandler
from models import Admin

from lib import qr, ziplib

from config import app_config as cfg
from models import Location, Comfort
from google.appengine.api import memcache
from google.appengine.ext import db

MC_LOCATIONS_KEY = cfg.get('MC_LOCATIONS_KEY', '')
HOSTNAME = cfg.get('hostname', 'localhost')

def get_locations():
	locations = memcache.get(MC_LOCATIONS_KEY)
	if not locations:
		locations = list(Location.all())
		memcache.set(MC_LOCATIONS_KEY, locations)
	return locations

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
		locations = get_locations()
		buildings = set([location.building for location in locations])
		self.render('admin/main', admin=admin, buildings=buildings, building=building)


class RoomsHandler(AdminHandler):
	def render_locations(self, template, **kwargs):
		locations = get_locations()
		self.render(template, locations=locations, **kwargs)

	@login_required
	def get(self):
		self.render_locations('admin/rooms')
		return


class DeleteRoomsHandler(RoomsHandler):

	@login_required
	def post(self):
		rooms_to_delete = json.loads(self.request.body)
		if not rooms_to_delete:
			self.redirect('/rooms')
			return

		locations = [Location.get_by_key_name(room) for room in rooms_to_delete]
		comforts = [c for c in Comfort.all()]

		for location in locations:
			comforts_to_remove = filter(lambda c: c.loc_building == location.building and \
																						c.loc_floor == location.floor and \
																						c.loc_room == location.room,
																						comforts)
			db.delete(comforts_to_remove)
			db.delete(location)

		memcache.delete(MC_LOCATIONS_KEY)


class AddRoomsHandler(RoomsHandler):

	@login_required	
	def post(self):
		data = self.request.get('rooms')
		if not data:
			self.redirect('/rooms')

		rooms = [room.strip() for room in data.split('\n')]
		locations = filter(lambda room: room is not None,
											 [Location.create(room) for room in rooms])

		db.put(locations)
		memcache.delete(MC_LOCATIONS_KEY)

		self.render_locations('admin/rooms',
													msg="Successfully added the following locations",
													modified_locs=locations)


class QRCodesHandler(RoomsHandler):

	def color_for_level(self, level):
		if level == 2:
			return qr.COLORS['red']
		elif level == -2:
			return qr.COLORS['blue']
		else:
			return qr.COLORS['black']
	
	@login_required
	def get(self):
		self.render_locations('admin/qr')
		return

	@login_required
	def post(self):
		location_keys = [value for key, value in self.request.str_POST.iteritems() if key == 'location']		
		if not location_keys:
			self.redirect('/qr')
			return

		files = []
		size = '450x450'

		for key in location_keys:
			for level in [-2, 0, 2]:

				color = self.color_for_level(level)
				friendly_filename = "%s-%s.png" % (key.replace(':', '-'), color)
				url = '%s/api/qr/%s' % (HOSTNAME, key)
				if level != 0:
					url = '%s/%s' % (url, level)
				data = qr.generateQR(url, size, color=color)
				if data:
					files.append((friendly_filename, data))

		qr_codes = ziplib.create_with_files(files)

		self.response.headers['Content-Type'] = 'application/zip'
		self.response.headers['Content-Disposition'] = 'attachment; filename="qr_codes.zip"'
		self.response.out.write(qr_codes)
		return



class AdminAccountsHandler(AdminHandler):
	def render_admins(self, **kwargs):
		admin = self.get_admin()
		admins = list(Admin.all())
		self.render('admin/accounts', admin=admin, admins=admins, **kwargs)

	@login_required
	def get(self):
		self.render_admins()
		return


class DeleteAdminAccountsHandler(AdminAccountsHandler):

	@login_required
	def post(self):
		admins_to_delete = json.loads(self.request.body)
		if not admins_to_delete:
			self.redirect('/admins')
			return

		admins = [Admin.get_by_key_name(name) for name in admins_to_delete]
		db.delete(admins)


class AddAdminAccountsHandler(AdminAccountsHandler):

	@login_required
	def post(self):
		name = self.request.get('name')
		password = self.request.get('password')
		confirm = self.request.get('password-confirm')
		display = self.request.get('display')

		if name and password and confirm:
			other = Admin.all().filter('name = ', name).get()
			if not other and password == confirm:
				a = Admin.register(name, password, display=display)
				a.put()
				self.render_admins(msg="Successfully added new admin: %s" % name,
													 type="success")
				return

		self.render_admins(msg="You must fill in a unique username, password, and confirmation",
											 type="danger")
		return


class AccountHandler(AdminHandler):

	@login_required
	def get(self):
		admin = self.get_admin()
		self.render('admin/account', admin=admin)