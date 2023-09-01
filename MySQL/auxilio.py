import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Vinicius",
    password="dados123",
    database="mydatabase"
)

### CRIAR TABELA USUARIOS ###
mycursor = mydb.cursor()
sql = """
CREATE TABLE usuarios ( 
    id INT AUTO_INCREMENT PRIMARY KEY,                       
    nome VARCHAR(255),
    fav VARCHAR(255)
)
"""
mycursor.execute(sql)

### CRIAR TABELA PRODUTOS ###
sql = """
CREATE TABLE produtos ( 
    id INT(11),                       
    nome VARCHAR(255)
)
"""
mycursor.execute(sql)

### INSERIR REGISTROS DE USUARIOS ###
sql = """
INSERT INTO usuarios (id, nome, fav)
    VALUES (NULL, %s, %s)
"""

val = [
    ("Vinícius", "154"),
    ("Vitor", "155"),
    ("Adriana", ""),
    ("Wagner", ""),
]

mycursor.executemany(sql, val)
mydb.commit()

### INSERIR REGISTROS DE PRODUTOS ###
sql = """
INSERT INTO produtos (id, nome)
    VALUES (%s, %s)
"""

val = [
    ("154", "Chocolate"),
    ("155", "Chiclete"),
    ("156", "Bala")
]

mycursor.executemany(sql, val)
mydb.commit()