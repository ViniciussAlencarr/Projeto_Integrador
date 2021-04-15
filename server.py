import json
import requests
import mysql.connector

url = 'https://www.soawebservices.com.br/restservices/test-drive/serasa/concentre.ashx'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="sistema"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM app_ficha_cadastral")
myresult = mycursor.fetchone()




myObj = {
    "Credenciais": {
      "Email": '{email}',
      "Senha": '{password}'.format(email = myresult[1], password = myresult[3])
    },
    "Documento": "99.999.999/9999-62 ",
    "Adicionais": [
      1,
      2,
      3,
      4
    ]
  }

request = requests.post(url, json=myObj)

print(request.text)