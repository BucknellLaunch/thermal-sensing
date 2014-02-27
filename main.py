import webapp2

from routes import route_list
from config import app_config

application = webapp2.WSGIApplication(route_list,
																			config=app_config,
																			debug=app_config.get('debug', False))
