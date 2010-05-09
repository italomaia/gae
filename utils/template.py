# -*- coding:utf-8 -*-

__autor__="Italo MC Maia"

#
# template.py é responsável por criar o ambiente jinja2
# que fará a renderização dos templates
#

#--- Python Imports ---
from os import path
import logging
import sys

#--- Framework Imports ---
from jinja2 import FileSystemLoader as Loader
from jinja2 import Environment

#--- App Imports ---
import config

from utils import custom_filters
from utils import custom_tests
from utils import custom_extensions

def render(template_path, template_dict={}, debug=False):
    "Renderiza o template a partir de um arquivo de template"
    logging.debug("Renderizando '%s' do arquivo" % template_path)
    
    template = env.get_template(template_path)
    return template.render(template_dict)

def render_from_string(template_str, template_dict={}, debug=False):
    "Renderiza o template a partir de uma string"
    logging.debug("Renderizando a partir de uma string")
    
    template = env.from_string(template_str)
    return template.render(template_dict)

def register_rsc(what, env, _module):
    """
    what - filter ou test, informa o que se está registrando
    env - ambiente jinja2
    _module - módulo com os recursos desejados
    """
    for attr_name in dir(_module):
        attr = getattr(_module, attr_name)
        if callable(attr) and getattr(attr, "is_%s" % what, False):
            logging.debug("Registrando %s : %s" % (what, attr_name) )
            env.filters[attr_name]=attr

def get_extensions(_module):
    from jinja2.ext import Extension
    ext_list = []
    for attr_name in dir(_module):
        attr = getattr(_module, attr_name)
        if issubclass(attr.__class__, Extension):
            ext_list.append(attr)
    return ext_list

# obtendo a lista de extensões definidas
ext_list = get_extensions(custom_extensions)

# os templates do projeto devem estar na pasta template na raíz do projeto
env = Environment(loader=Loader(config.TEMPLATES_DIR), extensions=ext_list )

# adicionando as variáveis globais do ambiente
env.globals.update(config.SITE)

# registrando recursos
register_rsc("filter", env, custom_filters)
register_rsc("test", env, custom_tests)
