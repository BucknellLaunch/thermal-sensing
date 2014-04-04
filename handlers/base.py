import os
import json

import jinja2
import webapp2
 
import datetime as dt

from models import Admin
from lib import encrypt

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
															 autoescape = True)

class BaseHandler(webapp2.RequestHandler):
 def write(self, *a, **kw):
	self.response.write(*a, **kw)

 def render_str(self, template, **params):
	t = jinja_env.get_template(template)
	return t.render(params, admin=self.admin)

 def render(self, template, **kw):
	if not template.endswith('.html'):
	 template = template + '.html'
	self.response.write(self.render_str(template, **kw))

 def render_json(self, pydata):
	json_txt = json.dumps(pydata)
	self.response.headers['Content-Type'] = 'application/json'
	self.write(json_txt)

 def set_expiration_cookie(self, name, expiration_time):
 	self.response.set_cookie(name, 'true', expires=expiration_time)

 def set_secure_cookie(self, name, val):
	cookie_val = encrypt.make_secure_val(val)
	self.response.set_cookie(name, cookie_val)

 def read_secure_cookie(self, name):
	cookie_val = self.request.cookies.get(name)
	return cookie_val and encrypt.check_secure_val(cookie_val)

 def initialize(self, *a, **kw):
	webapp2.RequestHandler.initialize(self, *a, **kw)
	aid = self.read_secure_cookie('admin_id')
	self.admin = aid and Admin.by_name(aid)
	self.json = self.request.url.endswith('.json')


class BaseAuthenticationHandler(BaseHandler):
 def login(self, admin):
	self.set_secure_cookie('admin_id', str(admin.key().name()))

 def logout(self):
	self.response.delete_cookie('admin_id')


class BaseComfortHandler(BaseHandler):
	def has_submitted_recently(self):
		return self.request.cookies.get('submission_timeout')

	def record_comfort(self, comfort):
		comfort.put()
		thirty_mins_from_now = dt.datetime.utcnow() + dt.timedelta(minutes = 30)
		self.set_expiration_cookie('submission_timeout', thirty_mins_from_now)
		self.redirect('/thanks')
		return