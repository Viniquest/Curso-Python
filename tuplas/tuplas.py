# uma tupla é uma coleção imutável

""" tupla = ("Caçador", "Bruxo", "Mago", "Mago")
print(tupla)

tupla2 = ("Carro",)
print(type(tupla2))

tupla3 = ("Carro")
print(type(tupla3))

tupla4 = (1,5,6,3,14)
tupla5 = (False, False, True)
tupla6 = ("Mago", "Gelo", 70, 407, True)

tupla7 = tuple(("Fogo", 412, 1.83)) """

# acessando itens da tupla

""" tupla1 = ("Caçador", "Bruxo", "Mago")
print(tupla1)
print(tupla1[2])
print(tupla1[0:2])

print("Mago" in tupla1)

if "Paladino" in tupla1:
    print("Sim, está presente.")
else:
    print("Não contém.") """

# atualizando tuplas

""" tupla1 = ("Caçador", "Bruxo", "Mago")
print(tupla1) """


# adicionando itens
""" lista = list(tupla1)
lista[1] = "Xamã"

tupla1 = tuple(lista)
print(tupla1)

lista = list(tupla1)
lista.append("Monge")

tupla1 = tuple(lista)
print(tupla1) """

""" tupla2 = ("Xamã",)
tupla1 += tupla2

print(tupla1) """

# removendo itens

""" lista = list(tupla1)
lista.remove("Mago")

tupla1 = tuple(lista)
print(tupla1)

del tupla1
print(tupla1) """

# descompactar tuplas

""" tupla = ("Caçador", "Bruxo", "Mago", "Xamã", "Guerreiro")
print(tupla) """

""" (tupla1, tupla2, tupla3) = tupla """
""" (tupla1, *tupla2, tupla3) = tupla """
""" print(tupla1)
print(tupla2)
print(tupla3) """

# iteração com loops através de uma tupla

""" tupla1 = ("Caçador", "Bruxo", "Mago")
print(tupla1) """

""" for x in tupla1:
    print(x) """

""" for i in range(len(tupla1)):
    print(tupla1[i]) """

""" i = 0
while i < len(tupla1):
    print(tupla1[i])
    i += 1 """

# junta tuplas

""" tupla1 = ("Caçador", "Bruxo", "Mago")
tupla2 = (37, 22, 70)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla4 = tupla1 * 3
print(tupla4) """