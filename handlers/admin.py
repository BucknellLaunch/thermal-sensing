from base import BaseHandler
from models import Admin

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
			return Admin.by_id(int(aid))

class DashboardHandler(AdminHandler):
	@login_required
	def get(self):
		admin = self.get_admin()
		self.render('admin/main', admin=admin)

class AccountHandler(AdminHandler):
	@login_required
	def get(self):
		admin = self.get_admin()
		self.render('admin/account', admin=admin)