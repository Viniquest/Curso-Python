import os

# leitura de arquivos

""" f = open("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\demofile.txt", "r", encoding="UTF-8")
#print(f.read())
#print(f.read(7))
#print(f.readline())

for x in f:
    print(x)

f.close() """

# gravando arquivos

#f = open("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\teste.txt", "x")

""" f = open("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\teste.txt", "a")
f.write("Anexando conteudo ao arquivo.\n")
f.close() """

""" f = open("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\teste.txt", "w")
f.write("Sobrescrevendo o conteudo do arquivo.\n")
f.close() """

""" f = open("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\teste.txt", "r")
print(f.read())
f.close() """

# excluindo arquivos

""" os.remove("C:\\Users\\NGI\\Desktop\\Curso Python\\manipulaçao de arquivos\\demofile.txt") """

# para excluir pastas que contém arquivos, deve-se importar shutil e usar o comando shutil.rmtree.