import datetime as dt
from base import BaseHandler
from models import Comfort

class ComfortHandler(BaseHandler):
	def get(self):
		self.render('comfort/index')

	def post(self):
		if self.request.cookies.get('submission_timeout'):
			self.redirect('whoops')
			return

		errors = dict()

		level = self.request.get('level')
		loc_string = self.request.get('location')

		try:
			level = int(level)
		except ValueError:
			errors['level'] = "You must choose a level."

		if not loc_string:
			errors['location'] = "You can't leave your location blank."

		if errors:
			self.render('comfort/index', errors=errors)
		else:
			c = Comfort.create(level, loc_string)
			if c:
				c.put()
				thirty_mins_from_now = dt.datetime.utcnow() + dt.timedelta(minutes = 30)
				self.set_expiration_cookie('submission_timeout', thirty_mins_from_now)
				self.redirect('thanks')
			else:
				errors = { 'location': loc_string + ' is not a valid location.' }
				self.render('comfort/index', errors=errors)


class ThanksHandler(BaseHandler):
	def get(self):
		self.render('comfort/thanks')


class WhoopsHandler(BaseHandler):
	def get(self):
		self.render('comfort/whoops')


class RecordsHandler(BaseHandler):
	def get(self):
		records = list(Comfort.all())
		self.render('comfort/records', records=records)