# coding: utf-8
from django.shortcuts import render_to_response, render, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from axes.decorators import watch_login

# @ ==>Un decorador es una funcion previa a tu funcion
@watch_login  # Decorador de vigilancia de login
def login_view(request):
    """
    Función que permite el inicio de sesión en el proyecto django
    """

    # Si hay un usuario forzamos la salida

    logout(request)
    username = password = ''

#   Bandera para realizar el seguimiento de si la entrada es válida o no

    login_failed = False

    if request.POST:
        my_username = request.POST['username'].replace('  ','').lower()
        my_password = request.POST['password']
        authenticate(username=my_username,password=my_password)

        if user in not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin/')

        else:
            login_failed = True
    return render_to_response('accounts/login.html',
                              {'login_failed':login_failed},
                              context_instance = RequestContext(request))
