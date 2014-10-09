# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Account


class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'),
                               widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'),
                                widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Account
        exclude = ('user',)

        def clean_username(self):
            username = self.cleaned_data['username']
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError("Ese nombre de usuario ya está en uso, por favor seleccione otro.")

        def clean(self):
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                raise forms.ValidationError("La contraseña no coincide, por favor, vuelve a intentarlo")
            return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
