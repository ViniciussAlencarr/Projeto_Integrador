from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14)
    estado_Civil = models.CharField(max_length=25)
    contato_SMS = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    senha_Cliente = models.CharField(max_length=15)
    nome_De_Usuario = models.CharField(max_length=40)
    email_Cliente = models.EmailField()

class Emprestimo_Valor(models.Model):
    qtde_Parcelas = models.IntegerField()

class Emprestimo(models.Model):
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None) # Chave estrangeira da classe Cliente
    valor = models.ForeignKey(Emprestimo_Valor, on_delete=models.CASCADE, default=None) # Chave estrangeira da classe Emprestimo_Valor
    data_Solicitacao = models.DateField()

class Pagamento(models.Model):
    form_Pag = models.CharField(max_length=20)

class Resultado(models.Model):
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    score_Cliente = models.IntegerField()

class Cliente_Pagamento(models.Model):
    id_Pag = models.OneToOneField(Pagamento, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Pagamento
    id_Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Cliente
    data_Pagamento = models.DateField()

class Localidade_Estado(models.Model):
    nome_Estado = models.CharField(max_length=20)

class Tipo_Logradouro(models.Model):
    tipo_Logradouro = models.CharField(max_length=15)
    id_Estado = models.ForeignKey(Localidade_Estado, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Localidade_Estado

class Endereco_Empresa_Cliente(models.Model):
    nome_Rua_Comercial = models.CharField(max_length=40)
    num_Rua_Comercial = models.IntegerField()
    id_Tipo_Logradouro = models.ForeignKey(Tipo_Logradouro, on_delete=models.CASCADE, default=None) # Chave estrangeira da classe Tipo_Logradouro

class Formulario(models.Model):
    id_Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Cliente
    id_Endereco_Empresa = models.ForeignKey(Endereco_Empresa_Cliente, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Endereco_Empresa_Cliente
    balancos = models.CharField(max_length=200)
    faturamento_Anual = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    doc_Contrato_Social = models.CharField(max_length=120)
    renda_Bruta_Anual = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    indice_Liquidez = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    doc_Indice_Dividas = models.CharField(max_length=60)
    rentabilidade_Investimentos = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    holerites_Doc = models.CharField(max_length=60)
    doc_Declaracao_IR = models.CharField(max_length=60)
    receita_Operacional = models.DateField()
    doc_Valores_Contabeis = models.CharField(max_length=40)

class Tipo_Telefone(models.Model):
    tipo_Telefone = models.CharField(max_length=15)

class Telefones_Cliente(models.Model):
    id_Tipo_Telefone = models.ForeignKey(Tipo_Telefone, on_delete=models.CASCADE, default=None) # Chave estrangeira da classe Tipo_Telefone
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)# chave estrangeira da classe Cliente
    numero_Telefone = models.CharField(max_length=11)

class Endereco_Cliente(models.Model):
    id_Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Cliente
    id_Tipo_Logradouro = models.ForeignKey(Tipo_Logradouro, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Tipo_Logradouro
    nome_Rua = models.CharField(max_length=40)
    num_Rua = models.IntegerField()
    complemento = models.IntegerField()
    cep = models.CharField(max_length=8)

class Agencia(models.Model):
    nome_Agencia = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    nome_Dono = models.CharField(max_length=40)
    logradouro = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)
    nome_Rua = models.CharField(max_length=40)
    numero_Rua = models.IntegerField()
    cep = models.CharField(max_length=8)
    doc_Contrato_Social = models.CharField(max_length=200)
    doc_Historia_Empresa = models.CharField(max_length=200)
    qtde_Func = models.IntegerField()
    qtde_Dep = models.IntegerField()
    qtde_Anunciantes = models.IntegerField()

class Administrador(models.Model):
    id_Agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Agencia
    nome_Adm = models.CharField(max_length=20)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None) # Chave estrangeira da classe Cliente

class Sistema_Rn(models.Model):
    id_Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Cliente
    id_Resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Resultado
    id_Agencia = models.OneToOneField(Agencia, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Agencia 


class Localidade_Cidade(models.Model):
    id_Estado = models.ForeignKey(Localidade_Estado, on_delete=models.CASCADE, default=None) # chave estrangeira da classe Localidade_Estado
    nome_Cidade = models.CharField(max_length=20)

class Localidade_Bairro(models.Model):
    id_Localidade_Cidade = models.OneToOneField(Localidade_Cidade, on_delete=models.CASCADE, default=None) # chave estrangiera da classe Localidade_Cidade
    nome_Bairro = models.CharField(max_length=20)






