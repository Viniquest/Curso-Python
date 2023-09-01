a = 'Vinícius'
b = "Vinícius"
# em caso de str com mais de uma linha, é necessário estar entra ''' ou """
c = """ Jealousy, turning saints into the sea
Swimming through sick lullabies
Choking on your alibis
But it's just the price I pay
Destiny is calling me
Open up my eager eyes
'Cause I'm Mr. Brightside """
d = '''Jealousy, turning saints into the sea
Swimming through sick lullabies
Choking on your alibis
But it's just the price I pay
Destiny is calling me
Open up my eager eyes
'Cause I'm Mr. Brightside'''

#print(d)

e = "Mr Brightside"

#print(e)

#for x in "Gilgamesh":
#    print(x)

#x = len(e)
#print(len(e))

txt = "Você não está preparado!"

x = "preparado" in txt
print(x)
print("carro" in txt)

if "preparado" in txt:
    print("Sim, 'preparado' está presente!")

if "carro" not in txt:
    print("Não, 'carro' não está presente!")