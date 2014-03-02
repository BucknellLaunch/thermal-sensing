from datetime import datetime

from lib import errors
from base import BaseHandler
from models import Comfort, Location, Admin
from google.appengine.api import memcache

MC_LOCATIONS_KEY = 'LOCATIONS'

GREATER_THAN = 'g'
LESS_THAN = 'l'

FROM = 'from'
TO = 'to'

DELIMITER = '-'

class LocationsAPI(BaseHandler):
	def get(self):
		"""The API to get the list of locations from the database. The following
		parameters can be specified:
			building 		- (optional) the list of locations for the building
			floor 			- (optional) the list of locations for the building and floor
		Returns a list of locations in JSON format. An empty list will be returned
		if there are no results for the specified parameters."""
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
	def initialize(self, *a, **kw):
		BaseHandler.initialize(self, *a, **kw)
		self.error_code = None


	def get(self):
		"""The API to get comfort records from the database. Allows for the following
		parameters:
			key 			- (required) the admin's API key
			location 	- (optional) the location to get data from
			level 		- (optional) the level of comfort (can be specified as a range)
			from 			- (optional) the time to go from
			to 				- (optional) the time to go to
		The response is returned as a JSON object with the data requested, or an
		error with a description.
		"""
		key = self.request.get('key')
		a = Admin.by_api_key(key)
		if not a:
			self.render_json(errors.INVALID_KEY)
			return

		location = self.request.get('location')
		comforts = self.comforts_by_location(location)

		level = self.request.get('level')
		level_filter = self.create_level_filter(level)
		if level_filter:
			comforts = filter(level_filter, comforts)

		frm = self.request.get('from')
		frm_filter = self.create_date_filter(frm, FROM)
		if frm_filter:
			comforts = filter(frm_filter, comforts)

		to = self.request.get('to')
		to_filter = self.create_date_filter(to, TO)
		if to_filter:
			comforts = filter(to_filter, comforts)
		
		if self.error_code:
			self.render_json(self.error_code)
		else:
			self.render_json([comfort.as_dict() for comfort in comforts])
		a.record_api_access()


	def comforts_by_location(self, location):
		"""Gets the comfort records for a location. Looks for a location in the
		format '<building>-<floor>-<room>', '<building>-<floor>', or '<building>'
		and pulls the specified records from the database. If no location is specified,
		pulls all records"""
		if not location:
			comforts = [comfort for comfort in Comfort.all()]
		else:
			location_identifiers = tuple(location.split(DELIMITER))
			if len(location_identifiers) == 3:
				comforts = Comfort.by_room(*location_identifiers)
			elif len(location_identifiers) == 2:
				comforts = Comfort.by_floor(*location_identifiers)
			elif len(location_identifiers) == 1:
				comforts = Comfort.by_building(*location_identifiers)
			else:
				self.error_code = errors.INVALID_LOCATION_FORMAT
				return []
		return comforts


	def create_level_filter(self, level):
		"""Creates the function to use as a filter for the level. GAE does not allow
		for range queries with more than one inequality filter. If no inequality is
		specified, it returns a function that filters for equality."""
		if not level:
			return None

		try:
			level_int = int(level)
			f = lambda c: c.level == level_int
		except ValueError:
			qualifier = level[0]
			try:
				level_int = int(level[1:])
			except ValueError:
				self.error_code = errors.INVALID_LEVEL
				return None

			if qualifier == GREATER_THAN:
				f = lambda c: c.level > level_int
			elif qualifier == LESS_THAN:
				f = lambda c: c.level < level_int
			else:
				self.error_code = errors.INVALID_LEVEL_QUALIFIER
				return None

		if not level_int in range(-3, 4):
			self.error_code = errors.INVALID_LEVEL
			return None
		return f


	def create_date_filter(self, date, filter_type):
		"""Creates the function to use as a filter for the date. The filter_type
		can be either FROM or TO (specifying a range from or to a certain date).
		The date argument must be in the format 'MM-DD-YYYY', 'MM-YYYY', or 'YYYY'.
		"""
		if not date:
			return None
		
		date_identifiers = date.split(DELIMITER)
		if len(date_identifiers) == 3:
			format = "%m-%d-%Y"
		elif len(date_identifiers) == 2:
			format = "%m-%Y"
		else:
			format = "%Y"

		try:
			d = datetime.strptime(date, format)
			if filter_type == FROM:
				return lambda c: c.timestamp >= d
			else:
				return lambda c: c.timestamp <= d
		except ValueError:
			self.error_code = errors.INVALID_DATE_FORMAT
			return None