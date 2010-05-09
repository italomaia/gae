# -*- coding:utf-8 -*-

#--- App Imports ---
import view
from . import restful

#--- Framework Imports ---
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.api import urlfetch

#
# handlers são classes que respondem requisições do usuário
#

class MainHandler(restful.Controller):
    "Handler principal"
    def get(self):
        "this renders to main.html"
        page = view.ViewPage()
        user = users.get_current_user()
        return page.render(self, {"user":user})

class LoginHandler(restful.Controller):
    def get(self):
        page = view.ViewPage()
        return page.render(self)

class NotFoundHandler(restful.Controller):
    def get(self):
        "this renders to not_found.html"
        page = view.ViewPage()
        
        self.response.set_status(404)
        return page.render(self)

class UnauthorizedHandler(restful.Controller):
    
    def get(self): 
        "this renders to unauthorized.html"
        page = view.ViewPage()
        
        self.response.set_status(403)
        return page.render(self)
    
class ServerErrorHandler(restful.Controller):
    def get(self):
        "this renders to unauthorized.html"
        page = view.ViewPage()
        
        self.response.set_status(500)
        return page.render(self)