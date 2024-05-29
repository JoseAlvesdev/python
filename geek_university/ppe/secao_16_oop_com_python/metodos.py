"""
POO - Métodos

 - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja,
 as ações que esse objeto pode realizar no seu sistema.

 Em python, dividimos os métodos, em 2 grupos:
 Métodos de instância e Métodos de Classe.

 # Métodos de instância

# o método dunder init __init__ é um método especial chamado de
construtor e sua função e construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo under é chamado
de dunder (Double Underline)

OBS: Os metodos dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas própias funções utilizando dunder
(underline no início e no fim) não é aconselhado. Python possui vários métodos
com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas
funções mágicas internas da linguagem. Então, evite ao máximo, de preferência
nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

p1 = Produto('PlayStation', 'Video Game', 2300)

print(p1.desconto(50))

print(Produto.desconto(p1, 50)) # self, desconto

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade,):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __init__(self, nome, sobrenone, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenone
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


user = Usuario('José', 'Henrique', 'email@gmail.com', 'lk0k64h')
user2 = Usuario('Indiana', 'Jhones', 'email@gmail.com', 'lk0k64h')

print(user2.nome_completo())

print(Usuario.nome_completo(user)) # self (this)

print('Senha user:', user._Usuario__senha) # Acesso de forma errada de um atributo

# Cripotografar os dados