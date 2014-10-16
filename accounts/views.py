# coding: utf-8
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.generic import  FormView
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from axes.decorators import watch_login
from django.conf import settings
from .forms import SignUpForm

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


class SignUpView(FormView):
    success_url = '/dashboard/'
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def get_initial(self):
        # Forzando salida
        logout(self.request)

        return {'time_zone': settings.TIME_ZONE}

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()

        if form.is_valid():
            username = form.cleaned_data['username'].replace(' ', '').lower()
            password = form.cleaned:data['password']

            user = User.objects.create(username=username)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
