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
    url(regex=r'^signup/$', view=SignUpView.as_view, name='signup'),
    url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/accounts/login/'}, name=logout )

)

