def error(code, msg):
	return { 'error': code, 'message': msg }

INVALID_KEY = error(431, "Invalid API Key")