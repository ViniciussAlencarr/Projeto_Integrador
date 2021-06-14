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