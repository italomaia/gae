#-*- coding:utf-8 -*-

from apps import handlers

#
# O mapeamento de urls acontece aqui
#

ROUTES = [
    # caminho, handler
    ("/", handlers.MainHandler),
    ("/403.xhtml", handlers.UnauthorizedHandler),
    ("/404.xhtml", handlers.NotFoundHandler),
    ("/500.xhtml", handlers.ServerErrorHandler),
]

ROUTES+=[
    ("/.*", handlers.NotFoundHandler),
]