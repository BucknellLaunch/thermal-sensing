import errors
from base import BaseHandler
from models import Comfort, Location, Admin
from google.appengine.api import memcache

MC_LOCATIONS_KEY = 'LOCATIONS'

class LocationsAPI(BaseHandler):
	def get(self):
		locations = memcache.get(MC_LOCATIONS_KEY)

		if not locations:
			locations = list(Location.all())
			memcache.set(MC_LOCATIONS_KEY, locations)

		building = self.request.get('building')
		floor = self.request.get('floor')

		if building:
			if floor:
				f = lambda loc: loc.building == building and loc.floor == floor
			else:
				f = lambda loc: loc.building == building
			locations = filter(f, locations)

		self.render_json([str(location) for location in locations])


class DataAPI(BaseHandler):
	def get(self):
		key = self.request.get('key')
		a = Admin.by_api_key(key)
		if not a:
			self.render_json(errors.INVALID_KEY)

		location = self.request.get('location')
		if not location:
			comforts = [comfort for comfort in Comfort.all()]
		else:
			location_identifiers = tuple(location.split('-'))
			if (len(location_identifiers) == 3):
				comforts = Comfort.by_room(*location_identifiers)
			elif (len(location_identifiers) == 2):
				comforts = Comfort.by_floor(*location_identifiers)
			else:
				comforts = Comfort.by_building(*location_identifiers)
		
		self.render_json([comfort.as_dict() for comfort in comforts])
