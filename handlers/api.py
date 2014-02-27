from base import BaseHandler
from models import Comfort, Location
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
				print 'floor'
				f = lambda loc: loc.building == building and loc.floor == floor
			else:
				f = lambda loc: loc.building == building
			locations = filter(f, locations)

		self.render_json([str(location) for location in locations])