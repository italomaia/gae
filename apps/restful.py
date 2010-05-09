# -*- coding:utf-8 -*-

from google.appengine.ext import webapp

def get_sent_properties(request_func, propname_list):
    """
    This maps request strings to values in a hash, optionally run through
    a function with previous request values as parameters to the func.
    1) key -> just read in the corresponding request value
    2) tuple (key, func) -> Read the request value for the string key
        and pass it through func
    3) tuple (key, func, additional keys...) -> Get the request
        values for the additional keys and pass them through func
        before setting the key's value with the output.
    If a key is not present in the request, then we do not insert a key
    with None or empty string.  The key is simply absent, therefore allowing
    you to use the returned hash to initial a Model instance.
    """
    prop_hash = {}
    for item in propname_list:
        if isinstance(item, basestring):
            key = item
            value = request_func(item)
        elif isinstance(item, tuple):
            key = item[0]
            prop_func = item[1]
            if len(item) <= 2:
                value = prop_func(request_func(key))
            else:
                try:
                    addl_keys = map(prop_hash.get, item[2:])
                    value = prop_func(*addl_keys)
                except:
                    return None
        if value:
            prop_hash[key] = value
    return prop_hash

class Controller(webapp.RequestHandler):
    def get(self, *params):
        "Chamado para manipular uma solicitação HTTP GET"
        self.redirect("/403.xhtml")

    def post(self, *params):
        "Chamado para manipular uma solicitação HTTP POST"
        self.redirect("/403.xhtml")
    
    def put(self, *params):
        "Chamado para manipular uma solicitação HTTP PUT"
        self.redirect("/403.xhtml")
    
    def delete(self, *params):
        "Chamado para manipular uma solicitação HTTP DELETE"
        self.redirect("/403.xhtml")
    
    def options(self, *params):
        "Chamado para manipular uma solicitação HTTP OPTIONS"
        self.redirect("/403.xhtml")
    
    def head(self, *params):
        "Chamado para manipular uma solicitação HTTP HEAD"
        self.redirect("/403.xhtml")
    
    def trace(self, *params):
        "Chamado para manipular uma solicitação HTTP TRACE"
        self.redirect("/403.xhtml")
