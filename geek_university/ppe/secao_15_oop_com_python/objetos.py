"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto 
do mundo real para sua representação computacional, devemos criar quantos
objetos forem necessários. Podemos passar nos objetos/instâncias de uma classe
como variáveis do tipo definido na classe.

# Instâncias/Objetos
lamp1 = Lampada('Branca', 110, 60)

print(lamp1.checa_lampada())

lamp1.ligar_desligar()

print(lamp1.checa_lampada())

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'fel@email.com', '123=08')
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            self.__ligada = False


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(self.__cliente._Cliente__nome)


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cli1= Cliente('Angelina Jolie', '000.111.222-33')
cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()