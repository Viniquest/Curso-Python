# dictionaries são ordenadas, modificável, e não permite itens duplicados

""" dict1 = { 
    "Nome":"Vinícius",
    "Idade": 23,
    "Altura": 1.83,
    "Pais": ["Adriana", "Wagner"],
    123:True
    } """

""" print(dict1)
print(dict1["Idade"])
print(len(dict1))
print(type(dict1)) """

# acessando itens de um dictionary

""" dict1 = { 
    "Nome":"Vinícius",
    "Sobrenome": "Aquino da Cunha",
    "Idade": 23,
    "Altura": 1.83
    } """

""" x = dict1["Idade"]
print(x)
print(dict1["Idade"])
x = dict1.get("Idade")
print(x)
print(dict1.get("Idade"))

x = dict1.keys()
print(x)
dict1["Irmão"] = "Vitor"
print(x)

x = dict1.values()
print(x)

x = dict1.items()
print(x)
dict1["Idade"] = 24
print(x)

if "Idade" in dict1:
    print("Sim, 'Idade' é uma das chaves deste dictionary") """

# alterando itens

""" dict1 = { 
    "Nome":"Vinícius",
    "Sobrenome": "Aquino da Cunha",
    "Idade": 23,
    "Altura": 1.83
    } """

""" print(dict1)

dict1["Nome"] = "Vitor"
print(dict1)

dict1.update({"Idade": 18})
print(dict1) """

# adcionando itens

""" print(dict1)
dict1["Ano"] = 1999
print(dict1)

dict1.update({"Irmão": "Vitor"})
print(dict1) """

# removendo itens 

""" print(dict1) """
""" dict1.pop("Sobrenome") """
""" dict1.popitem() """
""" print(dict1) """

""" del dict1["Nome"] """
""" del dict1 """
""" dict1.clear() """
""" print(dict1) """

# loop em dictionary

""" dict1 = { 
    "Nome":"Vinícius",
    "Sobrenome": "Aquino da Cunha",
    "Altura": 1.83
    } """

""" for x in dict1:
    print(x) """

""" for x in dict1:
    print(dict1[x]) """

""" for x in dict1:
    print(x)
    print(dict1[x]) """

""" for x in dict1.values():
    print(x)

for x in dict1.keys():
    print(x) """

""" for x,y in dict1.items():
    print(x,y) """

# copiar dictionary

""" dict1 = { 
    "Nome":"Vinícius",
    "Sobrenome": "Aquino da Cunha",
    "Altura": 1.83
    }
print(dict1)

dict2 = dict1.copy()
print(dict2)

dict3 = dict(dict1)
print(dict3) """

# dicionarios alinhados

""" myFamily = {
    "filho1" : {
        "Nome": "Vinícius",
        "Idade": 23
    },
    "filho2" : {
        "Nome": "Vitor",
        "Idade": 18
    }
}

print(myFamily)

filho1 = {
    "Nome": "Vinícius",
    "Idade": 23
}

filho2 = {
    "Nome": "Vitor",
    "Idade": 18   
}

myFamily2 = {
    "filho1": filho1,
    "filho2": filho2
}

print(myFamily2) """