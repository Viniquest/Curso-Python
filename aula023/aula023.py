# operadores de identidade
""" x = ["laranja", "roxo"]
y = ["laranja", "roxo"]
z = x

print(x is z)
print(x is y) # testa o objeto, portanto false
print( x == y) # testa o conteudo, portanto true

print(x is not z)
print(x is not y)
print(x != y) """

# operadores de associação
a = ["goiaba", "laranja"]
print("laranja" in a) # checa se o valor esta presente na variável
print("laranja" not in a) # checa se o valor não esta presente na variável

print("jabuticaba" in a)
print("jabuticaba" not in a)

b = [3, 7, 19]
print(3 in b)
print(3 not in b)