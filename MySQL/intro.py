# conectando ao servidor

import mysql.connector

"""mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) """

# criando tabelas (VARCHAR()=campo para texto)

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor() 

sql = "CREATE TABLE pessoas(nome VARCHAR(255), idade INT(2))"

mycursor.execute(sql) """

""" mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x) """

# alterar estrutura da tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255)"
#sql = "ALTER TABLE pessoas DROP sobrenome"
sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"

mycursor.execute(sql) """

# chave primária

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"

mycursor.execute(sql) """

# inserir dados na tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, 'Vinicius', 'Cunha', 23)"

sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, %s, %s, %s)"

#val = ("Vitor", "Aquino", "18")
#mycursor.execute(sql, val)

val = [
    ("Vinícius", "Aquino", "23"),
    ("Vitor", "Aquino", "18"),
    ("Adriana", "Aquino", "51"),
    ("Wagner", "Cunha", "57")
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s)")
print(mycursor.lastrowid) """

# selecionar dados em uma tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM pessoas "
sql = "SELECT nome, idade FROM pessoas"

mycursor.execute(sql)

#myresult = mycursor.fetchone()
#print(myresult)

myresult = mycursor.fetchall()

for x in myresult:
    print(x) """

# selecionar com filtro

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM pessoas WHERE sobrenome = 'Aquino'"
#sql = "SELECT * FROM pessoas WHERE id = '5'"
#sql = "SELECT * FROM pessoas WHERE idade > '30'"
#sql = "SELECT * FROM pessoas WHERE sobrenome LIKE '%qui%'"
sql = "SELECT * FROM pessoas WHERE sobrenome = %s"
sobrenome = ("Aquino",)

mycursor.execute(sql, sobrenome)

myresult = mycursor.fetchall()

for x in myresult:
    print(x) """

# classificando o resultado

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM pessoas ORDER BY idade"
sql = "SELECT * FROM pessoas ORDER BY idade DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x) """

# excluir registros da tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DELETE FROM pessoas WHERE id = %s"
val = ('5',)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "registro(s) excluído(s)") """

# excluir uma tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DROP TABLE pessoas"
# sql = "DROP TABLE IF EXISTS pessoas" para não gerar erro
mycursor.execute(sql) """

# atualizar registros da tabela

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "UPDATE pessoas SET nome = %s WHERE id = %s"
val = ("Vinícius", "1")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "registro(s) afetado(s)") """

# limite o resultado

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM pessoas LIMIT 2"
sql = "SELECT * FROM pessoas LIMIT 2 OFFSET 1"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x) """

# juntando tabelas

""" mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "SELECT usuarios.nome AS nome, produtos.nome AS favorito FROM usuarios JOIN produtos ON usuarios.fav = produtos.id"
sql = "SELECT usuarios.nome AS nome, produtos.nome AS favorito FROM usuarios LEFT JOIN produtos ON usuarios.fav = produtos.id"
#sql = "SELECT usuarios.nome AS nome, produtos.nome AS favorito FROM usuarios RIGHT JOIN produtos ON usuarios.fav = produtos.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x) """