# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from app.models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255}),
        }
        erros_messages = {
            'id': {
                'required': 'Erro no id'
            },
            'username': {
                'required': "Nome de usuário obrigatório"
            },
            'email': {
                'required': 'Email obrigatório'
            },
            'password': {
                'required': "Senha obrigatória"
            }
        }


class Cliente_Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' # indica que todos os campos do model serão utilizados
    

class Ficha_Cadastral_Form(forms.ModelForm):
    class Meta:
        model = Ficha_Cadastral
        fields = '__all__'


    
