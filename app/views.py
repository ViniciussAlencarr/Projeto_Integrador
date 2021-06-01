from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from app.models import *
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def splashScreen(request):    
    return render(request, 'loginScreen.html')

def cadastro(request):
    data = {}
    data['form'] = UserCreationForm(request.POST)
    data['emailField'] = UserModelForm()
    if 'email' in request.POST:
        mail = request.POST['email']
        cliente = Cliente()
        cliente.email_Cliente = mail
        cliente.save()
    if data['form'].is_valid():
        data['form'].save()
        return redirect('login')
    return render(request, 'clienteSide/fichaCadastral.html', data)
        
@login_required
def homeAdm(request):
    data = {}
    data['db_adm'] = Administrador.objects.order_by('id')[0]
    search = request.GET.get('search')
    if (search):
        data['db'] = Cliente.objects.filter(nome__icontains = search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'adm/admHomeScreen.html', data)
    
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

@login_required
def homeCliente(request):
    if User.is_authenticated:
        data = {}
        data['db'] = Cliente.objects.order_by('id')[0]
        return render(request,'clienteSide/clienteHomeScreen.html', data)
    else:
        data = {}
        data['db'] = Cliente()
        aux = data['db']
        aux.save()
        data['aux'] = aux
        return render(request, 'clienteSide/clienteHomeScreen.html', data)
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

def verificacao_adm(nomeAdm, senhaAdm):
    user = User()
    nameUser = user.username = nomeAdm
    passwordUser = user.password = senhaAdm
    data = Administrador.objects.create(nome_Adm=nameUser, senha_Adm=passwordUser)
    return redirect('login')

def login_adm(request):
    if request.method == 'POST':
        #pegando dados do formulário do html
        nomeAdm = request.POST['username_adm']
        senhaAdm = request.POST['password_adm']
        authenticacao = authenticate(username=nomeAdm,password=senhaAdm)
        verificacao_adm(nomeAdm, senhaAdm)
        if authenticacao is not None:
            login(request, authenticacao)
            return redirect('homeAdm')
    return render(request, 'loginScreen.html')

@login_required    
def logout_cliente(request, pk):
    db = Cliente.objects.get(pk = pk)
    db.delete()
    logout(request)
    return redirect('login')

@login_required    
def logout_adm(request, pk):
    db_adm = Administrador.objects.get(pk = pk)
    db_adm.delete()
    logout(request)
    return redirect('login')


@login_required
def solicitacoes(request):
    data = {}
    data['db'] = Emprestimo.objects.all()
    data['form'] = Emprestimo_Form(request.POST)
    if data['form'].is_valid():
        data['form'].save()
    else:
        form = Emprestimo_Form()
    return render(request, 'clienteSide/solicitacoes.html', data) 

@login_required
def docs(request):
    data = {}
    try:
        data['db'] = Formulario.objects.order_by('id')[0]
        search = request.GET.get('search')
        if (search):
            data['db'] = Formulario.objects.filter(nome__icontains = search)
        else:
            data['db'] = Formulario.objects.all()
    except:
        data['db'] = Formulario.objects.all()
    data['form'] = Formulario_Form(request.POST) 
    if data['form'].is_valid():
         data['form'].save() 
         return redirect('docs') 
    return render(request, 'clienteSide/documentos.html', data)