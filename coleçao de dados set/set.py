# coleção de dados do tipo set
# o tipo set são coleções não ordenadas e imutáveis

""" set1 = {"Nidalee", "Elise", "Diana"}
print(set1) """

""" set2 = {1, 4, 7, 11, 15}
set3 = {True, False, False}
set4 = {"abc", 2021, True, 36}
print(type(set4))

set5 = set(("Carro", "Moto", "Bike"))
print(set5) """

# acessando itens no set

""" set1 = {"Gabriel", "Danny", "Arthur"}
print(set1)

# print(set1[1]) Não podemos acessar pelo indice

for x in set1:
    print(x)

print("Danny" in set1) """

# adicionando itens no set

""" set1 = {"Gabriel", "Danny", "Arthur"}
print(set1)

# set1.add("Lucas")

# set2 = {"Lucas", "João"}
set2 = ["Lucas", "João"]
set1.update(set2)
print(set1) """

# removendo itens do set

""" set1 = {"Nidalee", "Elise", "Diana"}
print(set1) """

""" set1.remove("Elise") """
""" set1.discard("Elise") """
""" x = set1.pop()
print(x) """
""" set1.clear """
""" del set1 """

""" print(set1) """

# loop de um set

""" set1 = {"Nidalee", "Elise", "Diana"}
print(set1)

for x in set1:
    print(x) """

# juntar coleções do tipo set

""" set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "b"}
print(set1)
print(set2) """

""" set1.update(set2)
print(set1) """

""" set3 = set1.union(set2)
print(set3) """

""" set1.intersection_update(set2)
print(set1) """

""" set3 = set1.intersection(set2)
print(set3) """

""" set1.symmetric_difference_update(set2)
print(set1) """

""" set3 = set1.symmetric_difference(set2)
print(set3) """