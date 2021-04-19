from django.forms import ModelForm
from django.views.generic.list import ListView
from app.models import *

class Cliente_Form(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' # indica que todos os campos do model serão utilizados
    

class Ficha_Cadastral_Form(ModelForm):
    class Meta:
        model = Ficha_Cadastral
        fields = '__all__'

    
