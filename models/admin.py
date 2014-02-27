from lib import encrypt

from google.appengine.ext import db

class Admin(db.Model):
	display = db.StringProperty()
	name = db.StringProperty(required=True)
	passhash = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

	@classmethod
	def by_id(cls, uid):
		return cls.get_by_id(uid)

	@classmethod
	def by_name(cls, name):
		u = cls.all().filter('name = ', name).get()
		return u

	@classmethod
	def register(cls, name, pw, display=None):
		if not display:
			display = name
		pw_hash = encrypt.make_pw_hash(name, pw)
		return cls(display=display, name=name, passhash=pw_hash)

	@classmethod
	def login(cls, name, pw):
		u = cls.by_name(name)
		if u and encrypt.valid_pw(name, pw, u.passhash):
			return u