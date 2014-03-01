from models import Admin
from base import BaseAuthenticationHandler
from lib import valid


class LoginHandler(BaseAuthenticationHandler):
 def get(self):
	if not self.admin:
		self.render('admin/login')
	else:
		self.redirect('/dashboard')

 def post(self):
	username = self.request.get('username')
	password = self.request.get('password')

	a = Admin.login(username, password)

	if a:
		self.login(a)
		self.redirect('/dashboard')
	else:
		msg = "Invalid credentials."
		self.render('admin/login', error=msg)


class LogoutHandler(BaseAuthenticationHandler):
 def get(self):
	self.logout()
	self.redirect('/')