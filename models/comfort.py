from location import Location

from google.appengine.ext import db

class Comfort(db.Model):
	level = db.IntegerProperty(required=True)

	# location
	loc_building = db.StringProperty(required=True)
	loc_floor = db.StringProperty(required=True)
	loc_room = db.StringProperty()

	timestamp = db.DateTimeProperty(auto_now_add=True)


	@classmethod
	def create(cls, level, loc_string):
		location = Location.from_string(loc_string)
		if location:
			return cls(level = level,
								 loc_building = location.building,
								 loc_floor = location.floor,
								 loc_room = location.room)

	@classmethod
	def by_building(cls, building, query=None):
		if not query:
			query = cls.all()
		comforts = [comfort for comfort in query]
		return filter(lambda c: c.loc_building == building, comforts)

	@classmethod
	def by_floor(cls, building, floor, query=None):
		comforts = cls.by_building(building, query)
		return filter(lambda c: c.loc_floor == floor, comforts)

	@classmethod
	def by_room(cls, building, floor, room, query=None):
		comforts = cls.by_floor(building, floor, query)
		return filter(lambda c: c.loc_room == room, comforts)

	def as_dict(self):
		def location_dict():
			return { 'building': 	self.loc_building,
							 'floor':		 	self.loc_floor,
							 'room':			self.loc_room }

		DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
		return { 'location': 	location_dict(),
						 'level': 		self.level,
						 'timestamp': self.timestamp.strftime(DATE_FORMAT) }

	def __str__(self):
		return "Comfort level %d in %s" % (self.level, self.location)