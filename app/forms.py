from django.forms import ModelForm
from app.models import *

class Cliente_Form(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'sobrenome', 'cnpj', 'estado_Civil', 'contato_SMS', 'whatsapp'] # indica que todos os campos do model serão utilizados


class Ficha_Cadastral_Form(ModelForm):
    class Meta:
        model = Ficha_Cadastral
        fields = '__all__'

