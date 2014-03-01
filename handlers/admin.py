from base import BaseHandler
from models import Admin

class AdminHandler(BaseHandler):
	def get_admin(self):
		aid = self.read_secure_cookie('admin_id')
		if aid:
			return Admin.by_id(int(aid))

class DashboardHandler(AdminHandler):
	def get(self):
		if not self.admin:
			self.redirect('/login')
		
		admin = self.get_admin()
		self.render('admin/dashboard', admin=admin)