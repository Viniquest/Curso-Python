# loop while

""" i = 1

while i < 6:
    print(i)
    i += 1

print("Fim do programa.") """

# loop for

""" nomes = ['Diana', 'Elise', 'Jarvan IV']

for x in nomes:
    print(x)

for x in "Ola Mundo!":
    print(x)

print("Fim do programa.") """

# função range()

""" for x in range(10):
    print(x) """

""" for x in range(5,11):
    print(x) """

""" for x in range(3, 30, 3):
    print(x) """

""" print("Fim do programa.") """

# instrução break

""" i = 1

while i < 6:
    print(i)
    if (i == 3):
        break
    i+=1

lista = ["Diana", "Elise", "Nidalee"]
for x in lista:
    print(x)
    if (x == "Elise"):
        break """ 

# instrução continue

""" i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
 
lista = ["Diana", "Elise", "Nidalee"]

for x in lista:
    if x == "Elise":
        continue
    print(x) """

# loops alinhados

""" nomes = ["Vinícius", "Vitor"]
sobrenomes = ["Aquino", "da Cunha"]

for x in nomes:
    for y in sobrenomes:
        x = x + " " + y
    print(x) """

# declaração de passagem nos loops

""" print("Início")

for x in [0, 1, 2]:
    pass

print("Fim.") """