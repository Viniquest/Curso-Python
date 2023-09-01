# introdução a funções

""" def myFunction():
    print("Ola de dentro da função.")

def cumprimenta(nome):
    print("Ola ", nome)

def multiplica(x):
    return x * 5

myFunction()
cumprimenta("Vinícius")
result = multiplica(4)
print(result)
print(multiplica(5)) """

# parametros

""" def nomeCompleto(nome, sobrenome):
    print(nome + " " + sobrenome)

def listaNomes(*nomes):
    for x in nomes: # for para passar os nomes individualmente
        print(x)

nomeCompleto("Vinícius", "Cunha")
listaNomes("Diana", "Elise", "Nidalee") """

# argumentos de palavra chave

""" def nomes(primeiro, segundo, terceiro):
    print("O primeiro nome é", primeiro)
    print("O segundo nome é", segundo)
    print("O terceiro nome é", terceiro)

nomes("Vinícius", "Vitor", "Adriana")
nomes(segundo = "Vinícius", terceiro = "Vitor", primeiro = "Adriana")

def nomeCompleto(**nome): # exemplo para imprimir dictionary
    print(nome)
    for x in nome.values():
        print(x)

nomeCompleto(pri="Vinícius", seg="Aquino", ter="da Cunha") """

# valor padrão do parâmetro

""" def myFunction(pais = "Brasil"):
    print("Eu sou de " + pais)

myFunction()
myFunction("Panama")
myFunction("Japão") """

# passando uma lista como argumento

""" def myFunction(alimentos):
    for x in alimentos:
        print(x)

frutas = ["Laranja", "Goiaba", "Melancia", "Banana"]

myFunction(frutas)
myFunction(["peixe", "carne"]) """

# declaração de passagem

""" def myFunction():
    pass

myFunction()
print("Fim do programa") """

# recursividade

""" def repetir(n):
    for x in range(n):
        print("Olá Mundo!")

def repetirRecursivo(n):
    if n > 0:
        print("Olá Mundo Recursivo!")
        repetirRecursivo(n-1)

repetir(4)
repetirRecursivo(5 )"""

# expressões lambda

x = lambda a : a + 10

""" result = x(5)
print(result) """
""" print(x(5)) """

""" x = lambda a, b : a * b
print(x(2, 4)) """

""" def myFunc(n):
    return lambda a : a * n

meuDuplicador = myFunc(2)
print(meuDuplicador(11))

meuTriplicador = myFunc(3)
print(meuTriplicador(11)) """