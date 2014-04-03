from base import BaseHandler, BaseComfortHandler
from models import Comfort

class ComfortHandler(BaseComfortHandler):
	def get(self):
		self.render('comfort/index')

	def post(self):
		if self.has_submitted_recently():
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
				self.record_comfort(c)
			else:
				errors = { 'location': loc_string + ' is not a valid location.' }
				self.render('comfort/index', errors=errors)


class ThanksHandler(BaseHandler):
	def get(self):
		self.render('comfort/thanks')


class WhoopsHandler(BaseHandler):
	def get(self):
		self.render('comfort/whoops')