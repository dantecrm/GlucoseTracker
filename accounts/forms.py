# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Botton, Submit, Fieldset, HTML, Field
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.models import User
from glucoses.models import Unit
from timezone_field import TimeZoneFormField
from django.forms import ModelForm
from accounts.models import Account

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=75)
    glucose_unit = forms.ModelChoiceField(Unit.objects.all(), empty_label=None, label='Unidad de Glucosa')
    time_zone = TimeZoneFormField(label='Zona Horaria')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal col-xs-12 col-md-6 col-lg-5'
        self.helper.label_class = 'col-xs-4 col-md-4 col-lg-4'
        self.helper.field_class = 'col-xs-8 col-md-8 col-lg-8'

        self.helper.layout(
            Fieldset(
                'Cree su Cuenta'
                Field('username', autofocus=True),
                Field('password'),
                Field('first_name'),
                Field('email'),
                Field('glucose_unit'),
                Field('time_zone'),
            ),
            FormActions(
                Submit('submit', 'Crear mi cuenta',
                       css_class = 'btn-success pull-right'),
            ),
        )

# TAREA

# * Como enviar correo con gmail por medio de python shell, programa
# * Conocer las librerias que se utilizan para enviar email

# class RegistrationForm(ModelForm):
#     username = forms.CharField(label=(u'User Name'))
#     email = forms.EmailField(label=(u'Email Address'))
#     password = forms.CharField(label=(u'Password'),
#                                widget=forms.PasswordInput(render_value=False))
#     password1 = forms.CharField(label=(u'Verify Password'),
#                                 widget=forms.PasswordInput(render_value=False))

#     class Meta:
#         model = Account
#         exclude = ('user',)

#         def clean_username(self):
#             username = self.cleaned_data['username']
#             try:
#                 User.objects.get(username=username)
#             except User.DoesNotExist:
#                 return username
#             raise forms.ValidationError("Ese nombre de usuario ya está en uso, por favor seleccione otro.")

#         def clean(self):
#             if self.cleaned_data['password'] != self.cleaned_data['password1']:
#                 raise forms.ValidationError("La contraseña no coincide, por favor, vuelve a intentarlo")
#             return self.cleaned_data

# class LoginForm(forms.Form):
#     username = forms.CharField(label=(u'User Name'))
#     password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
