#-*- coding:utf-8 -*-

import os

# projeto em modo debug?
DEBUG=os.environ['SERVER_SOFTWARE'].startswith('Dev')

# caminho para a raíz do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# local onde estão os templates do projeto
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# template usado quando o template requisitado não existe
MISSING_TMPL="missing_template.xhtml"

# url para os arquivos estáticos do site
MEDIA_URL = u"/media/"

# extensão padrão para resolução de templates
DEFAULT_EXT="xhtml" # xhtml, xml...

# tempo de cache de um template
CACHE_TIME=0

DATE_FORMAT=""
TIME_FORMAT=""
DATE_TIME_FORMAT=""

#
# variáveis globais dos templates
# 
SITE = {
    # autor do projeto
    "AUTHOR":u"Your name",
    # texto que aparece na barra da janela do navegador
    "TITLE":u"Título das páginas html",
    # url para os arquivos estáticos do site
    "MEDIA_URL":MEDIA_URL,
    # email de contato
    "EMAIL":u"",
    # url para a raíz do projeto
    "ROOT_URL":u"http://your-app.appspot.com/",
    "MASTER_ATOM_URL":"",
    "CHARSET":"utf-8",
}
