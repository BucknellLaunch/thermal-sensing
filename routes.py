from handlers import *

route_list = [
	('/', ComfortHandler),
	('/thanks', ThanksHandler),
	('/whoops', WhoopsHandler),

	('/login', LoginHandler),
	('/logout', LogoutHandler),
	
	('/dashboard', DashboardHandler),
	('/account', AccountHandler),

	('/rooms', RoomsHandler),
	('/rooms/add', AddRoomsHandler),
	('/rooms/delete', DeleteRoomsHandler),

	('/admins', AdminAccountsHandler),
	('/admins/add', AddAdminAccountsHandler),
	('/admins/delete', DeleteAdminAccountsHandler),

	('/qr', QRCodesHandler),
	
	('/api/locations', LocationsAPI),
	('/api/data', DataAPI),
	('/api/qr/(.+?)(?:/(-?\d+))?', QRCodeAPI),
	('/api/graph', GraphAPI)
]

# ?: -- means we don't want it as a query parameter
