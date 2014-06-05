#!/usr/bin/python

import datetime
import sys
sys.path.append("/home/ubuntu/developer/google_appengine/")

import remote_api_shell

from dev_appserver import fix_sys_path
fix_sys_path()

from google.appengine.ext.remote_api import remote_api_stub
import getpass
import string

def auth_func():
  return (raw_input('Username:'), getpass.getpass('Password:'))


if len(sys.argv) < 3:
    print ("Usage: {} path/locations.json path/comforts.json".format(
        sys.argv[0]))
    exit(1)

remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_func,
                               'localhost')

from models import Admin, Location, Comfort

#if len(list(Admin.all())) == 0:
# add initial user, we do not backup the admin tabl
a = Admin.register('admin', 'default', display='admin')
a.put()

print 'ADMINS:'
for a in Admin.all():
    print a.display, a.name, a.passhash, a.created

import json

def from_utc(utcTime,fmt="%Y-%m-%dT%H:%M:%S"):
    """
    Convert UTC time string to time.struct_time
    """
    # change datetime.datetime to time, return time.struct_time type
    return datetime.datetime.strptime(utcTime, fmt)

for loc in json.load(open(sys.argv[1])):
    l = Location( building = string.capitalize(loc['building']),
                  floor = loc['floor'],
                  room = loc['room'])
    l.put()
    print (l)

for comf in json.load(open(sys.argv[2])):
    c = Comfort(loc_building = string.capitalize(comf['loc_building']),
                loc_floor = comf['loc_floor'],
                loc_room = comf['loc_room'],
                level = comf['level'],
                timestamp = from_utc(comf['timestamp']))
    c.put()
    print (c)


