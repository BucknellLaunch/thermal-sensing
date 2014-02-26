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
