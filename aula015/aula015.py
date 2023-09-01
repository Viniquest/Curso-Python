a = "Vinícius Cunha"
b = a.upper() # tudo maiúsculo
print(b)
print(a.lower()) # tudo minúsculo

a = "   Vinícius Cunha   "
print(">" + a.strip() + "<") # serve para cancelar os espaços presentes no str

a = "Vinícius Cunha"
print(a.replace( "Cunha", "Aquino"))

a = "Carro,Moto,Caminhão"

print(a.split(",")) # apresenta em forma de lista, separando os itens de acordo com o que foi sinalizado