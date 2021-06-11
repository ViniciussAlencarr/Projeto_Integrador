import json
import requests
import mysql.connector
import methodsSerasa as mts

url = 'https://www.soawebservices.com.br/restservices/test-drive/serasa/concentre.ashx'

# PEGANDO O EMAIL E A SENHA PARA FAZER A REQUISIÇÃO AO SERASA
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="a"
)
mycursor = mydb.cursor()
mycursor.execute("select * from app_cliente;")
dbResponse = mycursor.fetchone()

# CARREGANDO O TEMPLATE JSON PARA REQUEST
concent = open('app/requests_Serasa/concentre.json')
concentreRequest = json.load(concent)

credenciaisRequest = concentreRequest.get("Credenciais")

credenciaisRequest["Email"] = dbResponse[9]
credenciaisRequest["Senha"] = dbResponse[7]  

# FAZENDO REQUISIÇÃO AO SERASA
response = requests.post(url=url, json=concentreRequest)
response_json = json.loads(response.text)

if response_json["Status"] == True and response_json['Transacao']['CodigoStatusDescricao'] == 'Transacao realizada com sucesso':
  print("Tudo OK!")
  a = mts.score
  if mts.totalOcorrencias(response_json['TotalOcorrencias']) == 'True':
    x1 = 1
    a += 100
  else:
    x1 = 0
    a -= 50
  if mts.valorTotalOcorrencias(response_json['ValorTotalOcorrencias']):
    x2 = 1
    a += 100
  else:
    x2 = 0
    a -= 50
  if mts.pendenciasInternas(response_json['PendenciasInternas']['TotalOcorrencias'], response_json['PendenciasInternas']['Mensagem']):
    x3 = 1
    a += 150 
  else:
    x3 = 0
    a -= 100
  if mts.restricoesFinanceiras(response_json['RestricoesFinanceiras']['TotalOcorrencias'], response_json['RestricoesFinanceiras']['Mensagem']):
    x4 = 1
    a += 150
  else:
    x4 = 0
    a -= 100
  if mts.pendenciasFinanceiras(response_json['PendenciasFinanceiras']['TotalOcorrencias'], response_json['PendenciasFinanceiras']['Mensagem']):
    x5 = 1
    a += 150
  else:
    x5 = 0
    a -= 100
  if mts.pendenciasBacen(response_json['PendenciasBacen']['TotalOcorrencias'], response_json['PendenciasBacen']['PendenciasBacenDetalhe'], response_json['PendenciasBacen']['Mensagem']):
    x6 = 1
    a += 250
  else:
    x6 = 0
    a -= 200
  if mts.protestos(response_json['Protestos']['TotalOcorrencias'], response_json['Protestos']['ProtestosDetalhe'], response_json['Protestos']['Mensagem']):
    x7 = 1
    a += 250
  else:
    x7 = 0
    a -= 200
  if mts.acoesJudiciais(response_json['AcoesJudiciais']['TotalOcorrencias'], response_json['AcoesJudiciais']['AcoesJudiciaisDetalhe'], response_json['AcoesJudiciais']['Mensagem']):
    x8 = 1
    a += 250
  else:
    x8 = 0
    a -= 200
  if mts.acheiRecheque(response_json['AcheiRecheque']['TotalOcorrencias'], response_json['AcheiRecheque']['AcheiRechequeDetalhe'], response_json['AcheiRecheque']['Mensagem']):
    x9 = 1
    a += 250
  else:
    x9 = 0
    a -= 200
  if mts.convemDevedores(response_json['ConvemDevedores']['TotalOcorrencias'], response_json['ConvemDevedores']['Mensagem']):
    x10 = '1'
    a += 150
  else:
    x10 = 0
    a -= 100
else:
  print("Deu erro") 

""" if response.status_code >= 200 and response.status_code <=299:
  print('Status Code', response.status_code)
  print('Reason', response.reason)
  print('Text', response.text)
  print('JSON', response.json())
  jsonResponse = response.json()
else:
  print('Status Code', response.status_code)
  print('Reason', response.reason)
  print('Text', response.text)
  print('JSON', response.json())  """  