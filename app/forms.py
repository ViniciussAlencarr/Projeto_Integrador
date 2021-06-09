# -*- coding: utf-8 -*-
from django.db.models import fields
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

class Emprestimo_Form(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        exclude = ['situacao']
        
class Formulario_Form(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        exclude = ['id_Cliente', 'id_Endereco_Empresa']

class Pagamentos_Form(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['limite']
        
        
    
