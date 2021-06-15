import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="a"
)
try:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM app_resultado;")  
    dbResponse = mycursor.fetchone() 
    score = dbResponse[1] # score do cliente pego diretamente do banco dde dados na tabela 'app_resultado'
    aux = score
except:
    print("Parece que não há um limite definido... defina um limite e tente novamente.")

def totalOcorrencias(value):
    if value >= 0:
        return True
    else:
        return False 
    
def valorTotalOcorrencias(value):
    if value == '0,00':
        score+100
        return True
    else:
        score-50
        return False

def pendenciasInternas(value, value02):
    if value == 0 and value02 == 'NAO CONSTAM OCORRENCIAS':
        score+150
        return True
    else:
        score-100
        return False

def restricoesFinanceiras(value, value02):
    if value == 0 and value02 == 'NAO CONSTAM OCORRENCIAS':
        score+150
        return True
    else:
        score-100
        return False

def pendenciasFinanceiras(value, value02):
    if value == 0 and value02 == 'NAO CONSTAM OCORRENCIAS':
        score =+150
        return True
    else:
        score =-100
        return False

def pendenciasBacen(value, value02, value03):
    if value == 0 and value02 == None and value03 == 'NAO CONSTAM OCORRENCIAS':
        score+250
        return True
    else:
        score-200
        return False

def protestos(value, value02, value03):
    if value == 0 and value02 == None and value03 == 'NAO CONSTAM OCORRENCIAS':
        score+250
        return True
    else:
        score-200
        return False

def acoesJudiciais(value, value02, value03):
    if value == 0 and value02 == None and value03 == 'NAO CONSTAM OCORRENCIAS':
        score+250
        return True
    else:
        score-200
        return False

def acheiRecheque(value, value02, value03):
    if value == 0 and value02 == None and value03 == 'NAO CONSTAM OCORRENCIAS':
        score+250
        return True
    else:
        score-200
        return False

def convemDevedores(value, value02):
    if value == 0 and value02 == 'NAO CONSTAM OCORRENCIAS':
        score+150
        return True
    else:
        score-100
        return False