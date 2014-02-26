from base import BaseHandler

class ComfortHandler(BaseHandler):
 def get(self):
  self.render('comfort/index')

 def post(self):
  pass