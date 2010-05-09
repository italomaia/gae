Descrição dos arquivos da raíz do projeto
=========================================

A primeira é feita através do parâmetro -i ou --init, e a segunda
utilizando-se de -a ou --startapp. Em caso de dúvida, use o -h/--help.

## config.py ##
Possui as configurações do sistema, como variáveis globais, url padrão
para conteúdo estático, nome do autor, etc.

## módulo forms ##
Funções e classes que auxiliam na criação e utilização de formulário.

## main.py ##
Controla o aplicativo, fazendo o roteamento e carregando as bibliotecas
básicas.

## routing.py ##
O mapeamento de urls para handlers é feito neste arquivo.

## view.py ##
Ao contrátio do que acontece no django, o view.py serve para guardar algumas
funções e classe importantes. Basicamente, saiba que a class ViewPage está
neste arquivo e é com ela que você renderiza seus templates.

Descrição dos arquivos por módulo
==================================

** apps **
-----------
Os aplicativos do gae devem ficar nesta pasta.

** jinja2 **
-------------
Engine dos templates

#ref: http://jinja.pocoo.org/2/

** media_root **
-----------------
Por padrão, o conteúdo estático fica nesta pasta.

** models **
-----------
Algumas funções e classes utilizadas nos modelos ficam aí. Não coloque seus
modelos nesta pasta.

** simplejson **
------------------
Faz o parse para o formato json. 

#ref: http://pypi.python.org/pypi/simplejson

** templates **
-----------------
Todos os templates(arquivos html, xml, etc) ficam nesta pasta, separados em
subpastas. Alguns templates padrão já estão na raíz e devem ser conferidos.

** utils **
------------
Uma série de classes e funções utilitárias

** wtforms **
-------------
Permite a geração intuitiva de formulários.

# ref: http://wtforms.simplecodes.com/docs/0.6/ext.html#module-wtforms.ext.appengine




