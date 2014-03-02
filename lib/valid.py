import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def username(u):
	return u and USER_RE.match(u)

PASS_RE = re.compile(r"^.{3,20}$")
def password(p):
	return p and PASS_RE.match(p)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def email(e):
	return not e or EMAIL_RE.match(e)

LEVEL_RANGE = range(-3, 4)
def level(l):
	try:
		level_int = int(l)
	except ValueError:
		try:
			level_int = int(l[1:])
		except ValueError:
			return False
	return level_int in LEVEL_RANGE

def location(l, min_identifiers=1):
	identifiers = l.split('-')
	return len(identifiers) <= 3 and len(identifiers) >= min_identifiers