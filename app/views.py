from django.shortcuts import render, redirect
from app.forms import Cliente_Form, Ficha_Cadastral_Form

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = Ficha_Cadastral_Form()
    return render(request, 'form.html', data)

def create(request):
    form = Ficha_Cadastral_Form(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def createCliente(request):
    form = Cliente_Form(request.POST or None)
    if (form.is_valid()):
        form.save()
    return redirect('home')