from django.shortcuts import render, redirect
from app.models import Cliente, Ficha_Cadastral
from app.forms import Cliente_Form, Ficha_Cadastral_Form, UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def splashScreen(request):
    return render(request, 'loginScreen.html')

@login_required
def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('/form_User')
    return render(request, 'clienteSide/fichaCadastral.html', context)

@login_required
def home(request):
    data = {}
    search = request.GET.get('search')
    if (search):
        data['db'] = Cliente.objects.filter(nome__icontains = search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'adm/admHomeScreen.html', data)


def form(request):
    data = {}
    data['form'] = Ficha_Cadastral_Form()
    return render(request, 'clienteSide/cadastro.html', data)


def form_User(request):
    data = {}
    data['form_User'] = Cliente_Form()
    return render(request, 'clienteSide/fichaCadastral.html', data)

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
    return render(request, 'adm/visualizarCliente.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    data['form'] = Cliente_Form(instance=data['db'])
    return render(request, 'clienteSide/clienteSide/cadastro.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    form = Cliente_Form(request.POST or None, instance=data['db'])
    if (form.is_valid()):
        form.save()
    return redirect('home')

def login_cliente(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username_cliente'], password=request.POST['password_cliente'])
        if user is not None:
            login(request, user)
            return redirect('/home')
    return render(request, 'loginScreen.html' )

def login_adm(request):
    if request.method == 'POST':
        adm = authenticate(username=request.POST['username_adm'], password=request.POST['password_adm'])
        if adm is not None:
            login(request, adm)
            return redirect('/home')
    return render(request, 'loginScreen.html')
    
def logout_cliente(request):
    logout(request)
    return redirect('login')