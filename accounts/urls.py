# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

# Se esta instanciando del urls.py del proyecto
urlpatterns = patterns('',
    url(r'^register/$', 'accounts.views.AccountRegistration'),
    url(r'^login/$', 'accounts.views.LoginRequest'),
    url(r'^logout/$', 'accounts.views.LogoutRequest'),

)

#A mano: 10 caras
#Investigar Expresiones Regulares libros:
#Mencionar que librería se usa para expresiones regulares en python
#10 ejemplos python

# Curso:
# Nombres:
# Fecha:
