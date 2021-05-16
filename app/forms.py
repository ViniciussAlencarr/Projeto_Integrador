# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from app.models import *
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class Cliente_Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' # indica que todos os campos do model serão utilizados
    
class Agencia_Form(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = '__all__'

<<<<<<< HEAD
class Emprestimo_Form(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class Emprestimo_Valor_Form(forms.ModelForm):
    class Meta:
        model = Emprestimo_Valor
        fields = '__all__'


=======
>>>>>>> parent of 6a9b5d59 (criando a interface de solicitaçoes de emprestimo)



    
