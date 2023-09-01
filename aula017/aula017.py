# forma de concatenar uma variável str com int
idade = 23
txt = "Eu sou o Vinícius e tenho {} anos de idade"
print(txt.format(idade))

quantidade = 11.5
item = "torres"
valor = 1.83
minhaAposta = "Over de {} {} na odd {}"
# outraAposta = "Under de {0} {1} na odd {2}" exemplo para manipular os itens dentro do str

print(minhaAposta.format(quantidade, item, valor)) # a ordem que você indica as variáveis é a que ele coloca na str
