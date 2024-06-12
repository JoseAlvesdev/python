"""
POO - Abstração e Encapsulamento

O grande objeto da POO é encapsular nosso código dentro de um grupo
lógico e hierarquico utilizando classes.

Encapsular -> Cápsula


                classe
-------------------------------------
|                                  |
|       atributos e métodos        |
|                                  |
-------------------------------------

# Relembrando Atributos/Metodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um
atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenomeno chamado
Name Mangling, que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

# Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, 
escondendo atributos e métodos privados de usuário.

conta1 = Conta('Geek', 150, 1500)

print(conta1.numero, conta1.titular, conta1.saldo, conta1.limite, sep='\n')

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 999999999999999
conta1.limite = 99999999999999999999999999999999999999999999

print(conta1.numero, conta1.titular, conta1.saldo, conta1.limite, sep='\n')
print(conta1.__dict__)

conta1.extrato()

conta1._Conta__saldo = 0 # Name Mangling, tbm consiguemos alterar

print(conta1._Conta__saldo) # Name Mangling

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(-200)

print(conta1.__dict__)
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f'Saldo de {self.__saldo} '
            f'do titular {self.__titular} '
            f'com limite de {self.__limite}'
        )

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else: 
            print('Deposite um valor maior que 0!')

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente!')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferência por quem realizou

        # 2 - Adiconar o valor na conta de destino
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Angelina', 150, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()