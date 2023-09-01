import re

txt = "WoW é um jogo MMO RPG de 2004"

# Verificar se começa com "WoW" e termina com "RPG"

""" x = re.search("^WoW.*RPG$", txt)

if x:
    print("SIM! temos uma correspondência!")
else:
    print("Nenhuma correspondência!")

x = re.search("^A.*RPG$", txt)

if x:
    print("SIM! temos uma correspondência!")
else:
    print("Nenhuma correspondência!")

x = re.search("^WoW.*MMO$", txt)

if x:
    print("SIM! temos uma correspondência!")
else:
    print("Nenhuma correspondência!") """

# função search()

""" x = re.search("\s", txt)

print("O primeiro espaço em branco está na posição:", x.start())

x = re.search("Lenda", txt)

print(x) """

# função findall()

""" x = re.findall("m", txt)
print(x)

x = re.findall("lenda", txt)
print(x) """

# função split()

""" x = re.split("\s", txt)

print(x)

x = re.split("\s", txt, 2)

print(x) """

# função sub()

""" x = re.sub("\s", ".", txt)

print(x)

x = re.sub("\s", ".", txt, 2)

print(x) """

# objeto de correspondência

""" x = re.search(r"\bW\w", txt)
print(x)
print(x.span())
print(x.string)
print(x.group()) """

# metacaracteres

""" # [] um conjunto de caracteres "[a-m]"

x = re.findall("[M-W]", txt)
print(x)

# \ Sinaliza uma sequência especial (também pode ser usado para caracteres de escape) "\d"

x = re.findall("\d", txt)
print(x)

# . Qualquer caractere (exceto caractere de nova linha) "W..W"

x = re.findall("jo..o", txt)
print(x)

# ^ Começa com "^WoW"

x = re.findall("^WoW", txt)
print(x)

# $ acaba/termina com "2004$"

x = re.findall("2004$", txt)
print(x)

# * Zero ou mais ocorrencias "umx*"

x = re.findall("umx*", txt)
print(x)

# + Zero ou mais ocorrencias "umx+"

x = re.findall("umx+", txt)
print(x)

# {} Exatamente o npumero especificado de ocorrencias "RP{1}"

x = re.findall("RP{1}", txt)
print(x)

# | Ou "lenda|RPG"

x = re.findall("lenda|jogo", txt)
print(x) """

# sequencias especiais

""" txt = "WoW é um jogo MMO RPG de 2004"

# \A Retorna uma correspondência se os caracteres especificado estiverem no início da string

x = re.findall("\AWoW", txt)
print(x)

# \b Retrona uma correspondência onde os caracteres especificados estão no início ou no final de uma palavra r"\bjo" r"go\b"

x = re.findall(r"go\b", txt)
print(x)

# \B retorna uma correspondencia onde os caracteres especificados estão presentes, mas não no início nem no final de uma palavra

x = re.findall(r"\Bgo", txt)
print(x)

# \d retorna uma correspondencia onde a string contem digitos (numeros de 0 a 9) "\d"

x = re.findall("\d", txt)
print(x)

# \D retorna uma correspondencia onde a string NAO contem digitos (numeros de 0 a 9) "\D"

x = re.findall("\D", txt)
print(x)

# \s retorna uma correspondencia onde a string contem um caractere de espaço em branco "\s"

x = re.findall("\s", txt)
print(x)

# \S retorna uma correspondencia onde a stringa NAO contem um caractere de espaço em branco "\S"

x = re.findall("\S", txt)
print(x)

# \w retorna uma correspondencia em que a string contem qualquer caractere de palavra (letras de a a z, numeros de 0 a 9 e _) "\w"

x = re.findall("\w", txt)
print(x)

# \W retorna uma correspondencia em que a string contem NAO qualquer caractere de palavra (letras de a a z, numeros de 0 a 9 e _) "\W"

x = re.findall("\W", txt)
print(x)

# \Z retorna uma correspondencia se os caracteres especificados estiverem no final da string "2004\Z"

x = re.findall("2004\Z", txt)
print(x) """

