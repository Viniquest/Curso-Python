txt = "Somos os chamados \"vikings\" do norte." # usando "" no meio da str
print(txt)
txt = "Ola\nMundo!" # adiciona uma quebra de linha
print(txt) 
txt = "Ola\rMundo!" # apaga tudo q venha antes da \
print(txt) 
txt = "Ola\tMundo!" # adiciona uma tabulação (espaço maior)
print(txt)
txt = "Isso irá inserir um \\ (barra invertida)." # gerou uma barra invertida
print(txt) 
txt = 'It\'s alright.' # para adicionar uma aspas simples
print(txt) 
#Este exemplo apaga um caractere (backspace):
txt = "Ola \bMundo!"
print(txt) #Uma barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
#Uma barra invertida seguida por três inteiros resultará em um valor octal:
txt = "\110\145\154\154\157"
print(txt) 