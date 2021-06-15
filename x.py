import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="a"
)
mycursor = mydb.cursor()

def iniciar(nome):
    mycursor.execute("select id from auth_user where username = '{0}';".format(nome))
    dbResponse = mycursor.fetchone()
    return dbResponse

def pegarDocs():
  mycursor.execute('select * from app_formulario;')
  dbresponse = mycursor.fetchone()
  return len(dbresponse)

def pegarScore(username):
  mycursor.execute("select score_Cliente from app_resultado where nomeCliente = '{0}';".format(username))
  dbresponse = mycursor.fetchone()
  return dbresponse[0]
  mycursor.close()
  
def pegarCliente(username):
  try:
    #pegar informações de quem acabou de solicitar o empréstimo
    mycursor.execute("select * from app_cliente where nome_De_Usuario = '{0}';".format(username))
    dbresponse = mycursor.fetchone()
    return dbresponse
  except:
    print("Cliente inexistente...")

def atualizarSituação(retorno, username):
  mycursor = mydb.cursor()
  sql ="update app_emprestimo set situacao = '{0}' where nomeCliente = '{1}';".format(retorno, username)
  mycursor.execute(sql)
  mydb.commit()
  return mycursor

