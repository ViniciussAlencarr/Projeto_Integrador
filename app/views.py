from django.shortcuts import render, redirect
from app.models import Cliente
from app.forms import Cliente_Form, UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def splashScreen(request):    
    return render(request, 'loginScreen.html')

def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'clienteSide/fichaCadastral.html', {'form': form})
        
@login_required
def homeAdm(request):
    data = {}
    search = request.GET.get('search')
    if (search):
        data['db'] = Cliente.objects.filter(nome__icontains = search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'adm/admHomeScreen.html', data)
    
@login_required
def homeCliente(request):
    return render(request, 'clienteSide/clienteHomeScreen.html')
    
@login_required
def delete(request, pk):
    db = Cliente.objects.get(pk = pk).delete()
    return redirect('homeAdm')

@login_required
def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    return render(request, 'adm/visualizarCliente.html', data)

@login_required
def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    data['form'] = Cliente_Form(instance=data['db'])
    return render(request, 'clienteSide/cadastro.html', data)

@login_required
def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk = pk)
    form = Cliente_Form(request.POST or None, instance=data['db'])
    if (form.is_valid()):
        form.save()
    return redirect('homeAdm')

def verificacao(nome, senha):
    cliente = Cliente()
    verif_nome = cliente.nome_De_Usuario
    verif_senha = cliente.senha_Cliente
    if nome != verif_nome and senha != verif_senha:
        user = User()
        nameUser = user.username = nome
        passwordUser = user.password = senha
        data = Cliente.objects.create(nome_De_Usuario=nameUser, senha_Cliente=passwordUser)
    return redirect('login')

def login_cliente(request):
    if request.method == 'POST':
        #pegando dados do formulário do html
        nome = request.POST['username_cliente']
        senha = request.POST['password_cliente']
        authenticacao = authenticate(username=nome,password=senha)
        verificacao(nome, senha)
        if authenticacao is not None:
            login(request, authenticacao)
            return redirect('homeCliente')
    return render(request, 'loginScreen.html')

def login_adm(request):
    if request.method == 'POST':
        adm = authenticate(username=request.POST['username_adm'], password=request.POST['password_adm'])
        if adm is not None:
            login(request, adm)
            return redirect('homeAdm')
    return render(request, 'loginScreen.html')

@login_required    
def logout_cliente(request):
    logout(request)
    return redirect('login')