#-*- coding:utf-8 -*-

#--- Python Imports ---
import os, logging

#--- Framework Imports ---
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#--- App Imports ---
import config
import routing

logging.info('Loading %s, app version = %s',
             __name__, os.getenv('CURRENT_VERSION_ID'))

def main():
    application = webapp.WSGIApplication(routing.ROUTES, debug=config.DEBUG)
    run_wsgi_app(application)

if __name__=="__main__":
    main()
