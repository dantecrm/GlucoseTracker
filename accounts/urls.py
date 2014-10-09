# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib.auth.views import logout
from .views import login_view

# Se esta instanciando del urls.py del proyecto
urlpatterns = patterns('',
    url(regex=r'^login/$', view=login_view, name='login'),
    url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/accounts/login/'}, name=logout )

    # url(r'^login/$', 'accounts.views.LoginRequest'),
    # url(r'^register/$', 'accounts.views.AccountRegistration'),
    # url(r'^logout/$', 'accounts.views.LogoutRequest'),

)

#A mano: 10 caras
#Investigar Expresiones Regulares libros:
#Mencionar que librería se usa para expresiones regulares en python
#10 ejemplos python

# Curso:
# Nombres:
# Fecha:
