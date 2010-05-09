# -*- coding:utf-8 -*-

#
# Code based in the bloog project
# http://bloog.billkatz.com/
#

#--- Python Imports ---
import string
import logging
import mimetypes
from os import path

#--- Framework Imports ---
from google.appengine.api import users
from google.appengine.api import memcache

#--- App Imports ---

import config
from utils import template

guess_type = lambda filename: mimetypes.guess_type(filename)[0]

def to_filename(camelcase_str):
    """Reformata strings em CamelCase para camel_case

    >>> to_filename("AlgoAssim")
    algo_assim
    """
    filename = camelcase_str[0].lower()
    for ch in camelcase_str[1:]:
        if ch in string.uppercase:
            filename += '_' + ch.lower()
        else:
            filename += ch
    return filename

def get_view_file(handler, params={}):
    """Descobre o nome do arquivo baseado no nome da classe handler.
    Retorna uma tupla no formato (filename, content_type)
    
    Regra de resolução de nomes:
        apps.handlers.NomeHandler -> nome.ext
        apps.handlers.SobreNomeHandler -> sobre_nome.ext
        apps.modulo.handlers.NomeHandler -> modulo/nome.ext
        apps.modulo.outro.NomeHandler -> modulo/outro/nome.ext
        apps.modulo.modulo.modulo...outro.NomeHandler -> modulo/modulo/.../modulo/outro/nome.ext
    """
    cls = handler.__class__
    cls_name = cls.__name__
    module_name = cls.__module__
    
    if module_name.startswith('apps.') and \
        cls_name.endswith('Handler'):
        handler_path = module_name.split('.')[1:]
        
        if "handlers" in handler_path:
            handler_path.remove("handlers")
        
        handler_name = cls_name[:-7]
        template_path = handler_path + [to_filename(handler_name)]
        template_path = path.join(*template_path)
    else: raise Exception("Bad argument")
    
    template_path+= '.%s' % params.get("ext", config.DEFAULT_EXT)
    logging.info("template_path: "+template_path)
    return template_path, guess_type(template_path)

class ViewPage(object):
    "Classe base para os objetos restfull com cache!"
    def __init__(self, cache_time=None):
        "Inits the restful object with a 'cache_time'"
        self.cache_time = cache_time or config.CACHE_TIME

    def render_or_get_cache(self, handler, params):
        "Se a página está no cache, retorna. Senão, carrega e retorna."
        user = users.get_current_user()
        key = handler.request.url
        
        if self.cache_time and not user:
            try:
                data = memcache.get(key)
            except ValueError:
                data = None
            if data is not None:
                return data
        
        # template_info - (template, ctype)
        template_info = self.full_render(handler, params)
        
        if self.cache_time and not user:
            memcache.add(key, template_info, self.cache_time)
        return template_info

    def full_render(self, handler, params):
        "Carrega e popula o arquivo de template do handler"
        template_path, ctype = get_view_file(handler)
        full_template_path = path.join(config.TEMPLATES_DIR, template_path)
        
        # se o template não existe...
        if not path.exists( full_template_path ):
            logging.debug("template '%s' não existe." % full_template_path)
            
            if config.DEBUG:
                template_path = config.MISSING_TMPL
                ctype = guess_type(template_path)
                params = {"template":full_template_path}
                return template.render(template_path, params), ctype
            else: handler.redirect("/404.xhtml")
        
        return {
            "file":template_path,
            "body":template.render(template_path, 
                params, debug=config.DEBUG), 
            "content_type":ctype
        }

    def render(self, handler, params={}):
        """Obtém o template a partir do nome do handler
        e escreve no stream de saída"""
        template_info = self.render_or_get_cache(handler, params)
        
        # coloca o Content-Type correto e renderiza
        handler.response.headers["Content-Type"]=params.get("content_type", template_info["content_type"])
        handler.response.out.write(template_info["body"])
