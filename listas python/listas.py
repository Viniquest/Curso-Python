# introdução a listas
lista = ["Nidalee", "Fiddlesticks", "Elise", "Nidalee", "Diana", "Jarvan IV", "Vi"]
""" print(lista)
print(len(lista)) # quantidade de itens da lista

lista2 = [1,2,5,6,7,9]
lista3 = [True, True, False, True]
lista4 = ["Nidalee", 7, True]

print(type(lista))

lista5 = list(("Jungle", "Mid", "Adc"))
print(lista5) """

# acessando itens da lista

""" print(lista[2])

nome = lista[0]
print(nome)
print(lista[-1])
print(lista[1:5])
print(lista[:3])
print(lista[4:])

if "Diana" in lista:
    print("Sim, Diana está na lista") """

# alterar itens da lista

""" lista[3] = "Rengar"
print(lista)

lista[0:2] = "Rengar", "Kha Zix", "Graves"
print(lista) """

# adicionando itens na lista

""" lista.insert(2, "Graves") # é inserido antes do índice referido
print(lista)

lista.append("Rengar") # é adicionado no final da lista
print(lista)

lista.extend(['Fizz', 'Kassadin', 'Syndra'])
print(lista)

listaMid = ['Fizz', 'Kassadin', 'Syndra']
lista.extend(listaMid)
print(lista) """

# Remover itens da lista

lista = ["Nidalee", "Fiddlesticks", "Elise", "Nidalee", "Diana", "Jarvan IV", "Vi"]
""" print(lista) """

""" lista.remove("Fiddlesticks")
print(lista)

lista.pop(2)
print(lista)

lista.pop() # assim remove sempre o ultimo item
print(lista)

del lista[1]
print(lista)

del lista # apaga a lista toda, por isso da erro
print(lista) """

""" lista.clear()
print(lista) """

# iterando com loop nas listas

""" for x in lista:
    print(x) """

""" for i in range(len(lista)):
    print(lista[i]) """

""" i = 0
while i < 7:
    print(lista[i])
    i += 1 """

""" [print(x) for x in lista] """

""" print("Fim da execução.") """

# compreensão de lista

lista = ["Nidalee", "Fiddlesticks", "Elise", "Nidalee", "Diana", "Jarvan IV", "Vi"]

""" novaLista = []
for x in lista:
    if "a" in x:
        novaLista.append(x) """

""" novaLista = [x for x in lista if "a" in x] """
""" novaLista = [x for x in lista if x != "Nidalee"] """
""" novaLista = [x for x in lista] """
""" novaLista = [x for x in range(10) if x % 2 == 0] """
""" novaLista = [x.upper() for x in lista] """
""" novaLista = ["Magros" for x in lista] """
""" novaLista = [x if x != "Nidalee" else "Gragas" for x in lista] """

""" print(novaLista) """

# classificação de listas

listaNum = [3, 77, 7, 19, 23]

""" lista.sort()
listaNum.sort() """

""" lista.sort(reverse = True)
listaNum.sort(reverse = True) """

""" def myfunction(n):
    return abs(n - 30)

listaNum.sort(key = myfunction) """

#lista.sort(key = str.lower) serve para respeitar a ordem alfabetica mesmo se tiver palavras iniciando com letra minuscula

""" lista.reverse()
listaNum.reverse() """

""" print(lista)
print(listaNum) """

# copiar listas

lista = ["Nidalee", "Fiddlesticks", "Elise", "Nidalee", "Diana", "Jarvan IV", "Vi"]

""" outra = lista
lista.append("Rengar") """ # jeito errado

""" outra = lista.copy()
lista.append("Rengar") """

""" outra = list(lista)
lista.append("Rengar") """

""" print(lista)
print(outra) """

# juntando listas

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

""" lista3 = lista1 + lista2
print(lista3) """

""" for x in lista2:
    lista1.append(x)
print(lista1) """

lista1.extend(lista2)
print(lista1)