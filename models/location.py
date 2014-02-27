from string import capitalize

from google.appengine.ext import db

def parse_location(loc_string):
	identifiers = loc_string.lower().split()
	if len(identifiers) < 2:
		building = floor = room = ''
	elif len(identifiers) > 2:
		building = identifiers[0]
		floor = identifiers[2]
		room = None
	else:
		building = identifiers[0]
		room = identifiers[1]
		floor = room[0]

	if floor in '0bBgG':
		floor = 'G'
	return building, floor, room

def db_key(building, floor, room):
	if room is None:
		return ':'.join((building, floor))
	else:
		return ':'.join((building, floor, room))


class Location(db.Model):
	# Location entities will have the key of either:
	#		building:floor
	# 	building:floor:room
	#
	building = db.StringProperty(required=True)
	floor = db.StringProperty()	# floor can be G, 1, 2, 3, ...
	room = db.StringProperty()

	@classmethod
	def by_id(cls, loc_id):
		return cls.get_by_id(loc_id)

	@classmethod
	def from_string(cls, loc):
		key = db_key(*parse_location(loc))
		return cls.get_by_key_name(key)

	@classmethod
	def create(cls, loc):
		building, floor, room = parse_location(loc)
		key = db_key(building, floor, room)
		return cls(key_name=key, building=building, floor=floor, room=room)

	def __str__(self):
		if self.room is None:
			return "%s Floor %s" % (capitalize(self.building), self.floor)
		else:
			return "%s %s" % (capitalize(self.building), self.room)