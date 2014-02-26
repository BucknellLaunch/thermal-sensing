from handlers import *

route_list = [
        ('/', ComfortHandler),
        ('/login', LoginHandler),
        ('/logout', LogoutHandler)
]

# ?: -- means we don't want it as a query parameter
