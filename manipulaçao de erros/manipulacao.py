# try e except

""" try:
    print(x)
except:
    print("Exceção rolando")

print("continuando") """

# NameError

""" try:
    print(x)
except NameError:
    print("Variável x não definida")
except:
    print("Exceção rolando")

print("continuando") """

# Finally

""" x = "Ola Mundo!"

try:
    print(x)
except NameError:
    print("Variável x não definida")
except:
    print("Exceção rolando")
else:
    print("Tudo certo por aqui")
finally:
    print("O bloco try except foi finalizado")

print("continuando") """

# lançar uma exceção

""" x = 5

if x < 0:
    raise Exception("Não é permitido um número negativo.")

y = "Ola mundo!"

if not type(y) is int:
    raise TypeError("Somente números")

print("Fim do programa") """