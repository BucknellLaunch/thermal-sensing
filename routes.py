from handlers import *

route_list = [
	('/', ComfortHandler),
	('/thanks', ThanksHandler),
	('/records', RecordsHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/api/locations', LocationsAPI)
]

# ?: -- means we don't want it as a query parameter
