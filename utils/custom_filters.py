# -*- coding:utf-8 -*-

#
# para evitar que você crie um filtro que já existe, confira a lista
# de filtros que já vem com o jinja2
# http://jinja.pocoo.org/2/documentation/templates#list-of-builtin-filters
#

# igual aos filtros do django

import re
from utils import register_filter

# exemplo

# retirado direto do código do django
@register_filter
def slugify(value):
    "Passa uma string para o formato slug"
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)