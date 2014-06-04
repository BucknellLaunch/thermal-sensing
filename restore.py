#!/usr/bin/python

import sys
sys.path.append("/home/ubuntu/developer/google_appengine/")

import remote_api_shell

from dev_appserver import fix_sys_path
fix_sys_path()

from google.appengine.ext.remote_api import remote_api_stub
import getpass

def auth_func():
  return (raw_input('Username:'), getpass.getpass('Password:'))

remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_func,
                               'localhost')

from models import Admin

for a in Admin.all():
    print a.display, a.name, a.passhash, a.created

