# Igual a: x == y
# Diferente de: x != y
# Menor que: x < y
# Menor ou igual que: x <= y
# Maior que: x > y
# Maior ou igual a: x >= Y

""" x = 23
y = 73

if y < x:
    print("x é maior que y")
    print("outra intrução no if.")
elif x == y:
    print("x é igual a y")
elif x + 50 != y:
    print("x é diferente de y")
else:
    print("Todas as verificações retornam false")

print("Fim do programa.") """

# short hand if

""" x = 200
y = 100 """

""" if x > y: print("x é maior que y.") """

# short hand if else

""" print("sim") if x > y else print("não") """

""" print("sim") if x > y else print("=") if x == y else print("não")  """

# operadores lógicos

""" x = 200
y = 100
z = 500

if x > y and z > x:
    print("Ambas as condições são verdadeiras.")

if x < y or z > y:
    print("Uma das condições é verdadeira.") """

# estruturas condicionais alinhadas

""" x = 23

if x > 10:
    print("Maior do que 10")
    if x > 20:
        print("e também maior do que 20!")
        if x > 30:
            print("e também maior que 30!")
        else:
            print("mas não maior do que 30")
    else:
        print("Menor do que 20")
else:
    print("menor do que 10") """

# declaração de passagem

""" x = 50
y = 100

if x > y:
    pass

print("Fim do programa")
 """