# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from app.models import *
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name', 'last_name']

class Cliente_Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' # indica que todos os campos do model serão utilizados
    

class Ficha_Cadastral_Form(forms.ModelForm):
    class Meta:
        model = Ficha_Cadastral
        fields = '__all__'


    
