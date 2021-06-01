import json
import requests
import mysql.connector

url = 'https://www.soawebservices.com.br/restservices/test-drive/serasa/concentre.ashx'

# PEGANDO O EMAIL E A SENHA PARA FAZER A REQUISIÇÃO AO SERASA
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="sistema"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM app_ficha_cadastral")
dbResponse = mycursor.fetchone()

# CARREGANDO O TEMPLATE JSON PARA REQUEST
concent = open('app/requests_Serasa/concentre.json')
concentreRequest = json.load(concent)

credenciaisRequest = concentreRequest.get("Credenciais")
credenciaisRequest["Email"] = dbResponse[3]
credenciaisRequest["Senha"] = dbResponse[1]

# FAZENDO REQUISIÇÃO AO SERASA
response = requests.post(url=url, json=concentreRequest)

if response.status_code >= 200 and response.status_code <=299:
  print('Status Code', response.status_code)
  print('Reason', response.reason)
  print('Text', response.text)
  print('JSON', response.json())
  jsonResponse = response.json()
else:
  print('Status Code', response.status_code)
  print('Reason', response.reason)
  print('Text', response.text)
  #print('JSON', response.json())'''

