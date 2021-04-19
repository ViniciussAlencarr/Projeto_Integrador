from django.shortcuts import render, redirect
from app.models import Cliente, Ficha_Cadastral
from app.forms import Cliente_Form, Ficha_Cadastral_Form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def splashScreen(request):
    data = {}
    data['form'] = Ficha_Cadastral_Form()
    return render(request, 'home.html', data)
    
@login_required
def home(request):
    data = {}
    search = request.GET.get('search')
    if (search):
        data['db'] = Cliente.objects.filter(nome__icontains = search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = Ficha_Cadastral_Form()
    return render(request, 'exemplo.html', data)

def form_User(request):
    data = {}
    data['form_User'] = Cliente_Form()
    return render(request, 'form.html', data)

def create(request):
    form = Ficha_Cadastral_Form(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def createUser(request):
    form = Cliente_Form(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Cliente.objects.get(pk = pk).delete()
    return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    data['form'] = Cliente_Form(instance=data['db'])
    return render(request, 'exemplo.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    form = Cliente_Form(request.POST or None, instance=data['db'])
    if (form.is_valid()):
        form.save()
    return redirect('home')

def login_cliente(request):
    nome_De_Usuario = request.POST['nome_De_Usuario']
    senha_Cliente = request.POST['senha_Cliente']
    cliente = authenticate(request, nome_De_Usuario=nome_De_Usuario, senha_Cliente=senha_Cliente )
    if (cliente):
        return redirect('home')
    else:
        return redirect('form_User')


