#-*- coding:utf-8 -*-

# indica que a função decorada é um filtro do jinja2
def register_filter(fnc):
    fnc.is_filter = True
    return fnc

# indica que a função decorada é um teste do jinja2
def register_test(fnc):
    fnc.is_test=True
    return fnc

