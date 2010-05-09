#-*- coding:utf-8 -*-

import logging

from google.appengine.api import memcache
from google.appengine.ext import db

import config
import models

#---------------- Propriedades do AppEngine ----------------
#
# db.UserProperty               db.RatingProperty
# db.IntegerProperty            db.BlobProperty
# db.FloatProperty              db.TextProperty
# db.StringProperty             db.CategoryProperty
# ByteStringProperty            db.LinkProperty
# db.TimeProperty               db.EmailProperty
# db.DateProperty               db.GeoPtProperty
# db.DateTimeProperty           db.IMProperty
# db.SelectProperty             db.PhoneNumberProperty
# db.BooleanProperty            db.PostalAddressProperty
# db.ListProperty               db.ReferenceProperty
# db.StringListProperty         db.SelfReferenceProperty
#-----------------------------------------------------------


##########################################
# Exemplo de um modelo padrão do appengine
#
#class Modelo(db.Model):
#    conta_usuario = db.UserProperty("Conta", auto_current_user_add=True)
#    nome = db.StringProperty("Nome de usuário", required=True)
#    estado_civil = db.IntegerField(default=0, choices=[(0, 'solteiro'),(1, 'casado'),(2, 'divorciado')])
#    idade = db.IntegerField(required=True, validator=validators.positive_integer)
#
#    def __str__(self):
#        return u"Modelo"
#
##########################################

##########################################
# Exemplo de modelo serializável
#
#class Modelo(models.SerializableModel):
#
#    def __str__(self):
#        return u"Modelo"
#
##########################################