# jeito basico de classes e objetos

""" class myClass:
    x = 5

print(myClass)

p1 = myClass()
print(p1.x) """

# função init

""" class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Vinícius", 23)
print(p1.nome)
print(p1.idade)

p2 = Pessoa("Vitor", 18)
print(p2.nome)
print(p2.idade) """

# métodos de objeto

""" class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def myFunc(self):
        print("Ola meu nome é " + self.nome)

p1 = Pessoa("Vinícius", 23)
p1.myFunc()

p2 = Pessoa("Vitor", 18)
p2.myFunc() """

# o parametro self
# ele tem que ser sempre o primeiro parametro, mesmo podendo receber outro nome

""" class Pessoa:
    def __init__(meuObjeto, nome, idade) -> None:
        meuObjeto.nome = nome
        meuObjeto.idade = idade

    def myFunc(abc):
        print("Ola meu nome é " + abc.nome)

p1 = Pessoa("Vinícius", 23)
p1.myFunc() """

# modificar propriedades e declaração de passagem

# para não gerar erro no codigo, o pass
""" class Pessoa:
    pass

p1 = Pessoa() """

""" class Pessoa:
    def __init__(meuObjeto, nome, idade) -> None:
        meuObjeto.nome = nome
        meuObjeto.idade = idade

    def myFunc(abc):
        print("Ola meu nome é " + abc.nome)

p1 = Pessoa("Vinícius", 23)
p1.myFunc()

p1.nome = "Vitor"
p1.myFunc() """

# excluir objetos e propriedades

""" class Pessoa:
    def __init__(meuObjeto, nome, idade) -> None:
        meuObjeto.nome = nome
        meuObjeto.idade = idade

    def myFunc(abc):
        print("Ola meu nome é " + abc.nome)

p1 = Pessoa("Vinícius", 23)
print("Nome:", p1.nome)
print("Idade:", p1.idade) """

""" del p1.idade
print("Nome:", p1.nome)
print("Idade:", p1.idade) """

""" print(p1)
del p1
print(p1) """

# Herança

""" class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nomeCompleto(self):
        print(self.nome, self.sobrenome)

p1 = Pessoa("Vinícius", "Cunha")
p1.nomeCompleto()

class Estudante(Pessoa):
    pass

p2 = Estudante("Vitor", "Aquino")
p2.nomeCompleto() """

# função init na classe derivada

""" class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nomeCompleto(self):
        print(self.nome, self.sobrenome)

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
       # Pessoa.__init__(self, nome, sobrenome)
       # super().__init__(nome, sobrenome)

p1 = Estudante("Vinícius", "Cunha")
p1.nomeCompleto() """

# adicionar porpriedades e métodos

""" class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nomeCompleto(self):
        print(self.nome, self.sobrenome)

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, idade):
        super().__init__(nome, sobrenome)
        self.idade = idade
    
    def bemVindo(self):
        print("Bem vindo", self.nome, self.sobrenome)

x = Estudante("Vinícius", "Cunha", 23)
x.nomeCompleto()
print(x.idade)
x.bemVindo() """