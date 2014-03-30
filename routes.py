from handlers import *

route_list = [
	('/', ComfortHandler),
	('/thanks', ThanksHandler),
	('/whoops', WhoopsHandler),
	('/records', RecordsHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/dashboard', DashboardHandler),
	('/api/locations', LocationsAPI),
	('/api/data', DataAPI),
	('/api/qr/(.*?)/(\d+)', QRCodeAPI)
]

# ?: -- means we don't want it as a query parameter
