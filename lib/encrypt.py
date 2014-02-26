import random
import string

import hashlib
import hmac

from config import app_config as cfg

### COOKIE HASHING FUNCTIONS
SECRET = cfg['SECRET_KEY']

def hash_str(s):
  return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
  return "%s:%s" % (s, hash_str(s))

def check_secure_val(h):
  val = h.split(':')[0]
  if h == make_secure_val(val):
    return val


### PASSWORD HASHING FUNCTIONS
# use a string of 5 letters for the salt
def make_salt():
  return ''.join(random.choice(string.letters) for i in range(0,5))

# returns a password hash of the form "HASH,salt"
def make_pw_hash(user, pw, salt=None):
  if not salt:
    salt = make_salt()
  h = hashlib.sha256(user + pw + salt).hexdigest()
  return "%s,%s" % (h, salt)

# h is the entire hash string: "HASH,salt"
def valid_pw(user, pw, h):
  salt = h.split(',')[1]
  return make_pw_hash(user, pw, salt) == h
