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

	@classmethod
	def by_level(cls, level):
		pass

	@classmethod
	def by_level_greater_than(cls, level):
		pass

	@classmethod
	def by_level_less_than(cls, level):
		pass

	@classmethod
	def by_date_from(cls, date):
		pass

	@classmethod
	def by_date_to(cls, date):
		pass

	@classmethod
	def by_building(cls, building, query=None):
		if not query:
			query = cls.all()
		comforts = [comfort for comfort in query]
		return filter(lambda c: c.location.building == building, comforts)

	@classmethod
	def by_floor(cls, building, floor, query=None):
		comforts = cls.by_building(building, query)
		return filter(lambda c: c.location.floor == floor, comforts)

	@classmethod
	def by_room(cls, building, floor, room, query=None):
		comforts = cls.by_floor(building, floor, query)
		return filter(lambda c: c.location.room == room, comforts)

	def as_dict(self):
		DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
		return { 'location': 	self.location.as_dict(),
						 'level': 		self.level,
						 'timestamp': self.timestamp.strftime(DATE_FORMAT) }

	def __str__(self):
		return "Comfort level %d in %s" % (self.level, self.location)