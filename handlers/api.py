from base import BaseHandler
from models import Comfort, Location

class LocationsAPI(BaseHandler):
	def get(self):
		# check if its in the cache
		locations = [str(location) for location in Location.all()]
		self.render_json(locations)