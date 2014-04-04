from datetime import datetime
from lib import encrypt
from google.appengine.ext import db

API_KEY_LENGTH = 12

class Admin(db.Model):
	# Admin information (display name, username, password, date created)
	display = db.StringProperty()
	name = db.StringProperty(required=True)
	passhash = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

	# API information for the Admin
	api_key = db.StringProperty()
	api_requests = db.IntegerProperty(default=0)
	api_last_access = db.DateTimeProperty()

	def record_api_access(self):
		self.api_requests += 1
		self.api_last_access = datetime.now()
		db.put(self)

	@classmethod
	def by_id(cls, aid):
		return cls.get_by_id(aid)

	@classmethod
	def by_name(cls, name):
		a = cls.all().filter('name = ', name).get()
		if name:
			return cls.get_by_key_name(name)

	@classmethod
	def by_api_key(cls, api_key):
		a = cls.all().filter('api_key = ', api_key).get()
		return a

	@classmethod
	def register(cls, name, pw, display=None):
		if not display:
			display = name
		pw_hash = encrypt.make_pw_hash(name, pw)
		api_key = encrypt.random_hash()[:API_KEY_LENGTH]
		return cls(key_name=name, display=display, name=name, passhash=pw_hash, api_key=api_key)

	@classmethod
	def login(cls, name, pw):
		a = cls.by_name(name)
		if a and encrypt.valid_pw(name, pw, a.passhash):
			return a