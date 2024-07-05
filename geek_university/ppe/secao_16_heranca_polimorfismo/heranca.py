"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também estender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos 
outra classe que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe alguma entidade genérica o suficiente para encapsular
os atributos e métodos comuns a outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

OBS: Quando uma classe herda de outra classe ela herda todos os 
atributos e metodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe ela e chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe FIlha;
    - Classe Específica;

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comun de acessar dados da super classe
        self.__renda = renda
    

class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf,) # Forma comun de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jhones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na superclasse
ou em classe filhas.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comun de acessar dados da super classe
        self.__renda = renda

    def nome_completo(self):
        return f'{self._Pessoa__cpf} {super().nome_completo()}'
    

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf,) # Forma comun de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__matricula} {super().nome_completo()}'

# Sobrescrita de Métodos (Overriding)
cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jhones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())