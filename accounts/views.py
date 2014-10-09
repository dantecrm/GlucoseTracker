# coding: utf-8
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from axes.decorators import watch_login

from accounts.forms import RegistrationForm, LoginForm
from accounts.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

    if request.method == 'POST':
        usuario = request.POST['username'].replace('  ','').lower()
        clave = request.POST['password']
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin')
        else:
            login_failed = True
    return render_to_response('accounts/login_clase.html',
                              {'login_failed':login_failed},
                              context_instance = RequestContext(request))

# def AccountRegistration(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/profile/')
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
#             user.save()
#             account = Account(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
#             account.save()
#             return HttpResponseRedirect('/profile/')
#         else:
#             return render_to_response('accounts/register.html', {'form': form}, context_instance=RequestContext(request))
#     else:
#         ''' user is not submitting the form, show them a blank registration form '''
#         form = RegistrationForm()
#         context = {'form': form}
#         return render_to_response('accounts/register.html', context, context_instance=RequestContext(request))


# @login_required
# def Profile(request):
#     if not request.user.is_authenticated():
#         return HrttpResponseRedirect('/login/')
#     account = request.user.get_profile
#     context = {'account': account}
#     return render_to_response('accounts/profile.html', context, context_instance=RequestContext(request))


# def LoginRequest(request):
# 	if request.user.is_authenticated():
# 		return HttpResponseRedirect('/profile/')
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']
# 			account = authenticate(username=username, password=password)
# 			if account is not None:
# 				login(request, account)


# 				#cargando permisos de datos para el usuario
# 				request.session['id'] = "Hola"
# 				return HttpResponseRedirect('/profile/')
# 			else:
# 				return render_to_response('accounts/login_2.html', {'form': form}, context_instance=RequestContext(request))
# 		else:

# 			return render_to_response('accounts/login_2.html', {'form': form}, context_instance=RequestContext(request))
# 	else:
# 		''' user is not submitting the form, show the login form '''
# 		form = LoginForm()
# 		context = {'form': form}
# 		return render_to_response('accounts/login_2.html', context, context_instance=RequestContext(request))


# def LogoutRequest(request):
# 	logout(request)
# 	return HttpResponseRedirect('/')
