from location import Location

from google.appengine.ext import db

class Comfort(db.Model):
	level = db.IntegerProperty(required=True)
	timestamp = db.DateTimeProperty(auto_now_add=True)
	location = db.ReferenceProperty(Location,
																	collection_name="records",
																	required=True)

	@classmethod
	def create(cls, level, loc_string):
		location = Location.from_string(loc_string)
		if location:
			return cls(level=level, location=location)

	def __str__(self):
		return "Comfort level %d in %s" % (self.level, self.location)