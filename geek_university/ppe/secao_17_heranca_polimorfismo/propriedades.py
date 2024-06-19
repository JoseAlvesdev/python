"""
POO - Propriedades - Properties

Em linguagens de programção como o Java, ao declararmos atributos 
privados nas classes, costumamos a criar métodos públicos para a 
maninupalção desses atributos. Esses métodos são conhecidos por
getters e setters, onde os getters retornam o valor do atributo,
e os setters alteram o valor do mesmo.

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, value):
        self.__saldo += value

    def sacar(self, value):
        self.__saldo -= value

    def transferir(self, value, destino):
        self.__saldo -= value
        destino.__saldo += value

    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# print(conta1._Conta__saldo + conta2._Conta__saldo) # forma errada

print(conta1.get_saldo() + conta2.get_saldo())


print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

Forma que o professor costuma construir classes

class Exemplo:

    Atributos de classe

    Método Construtor e atributos de instância

    Propertys

    Métodos de instância

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter # [Propriedade | propriedade tipo (setter)]
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, value):
        self.__saldo += value

    def sacar(self, value):
        self.__saldo -= value

    def transferir(self, value, destino):
        self.__saldo -= value
        destino.__saldo += value

    # Usando um método como uma propriedade
    @property
    def valor_total(self):
        return self.__saldo + self.__limite



conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# print(conta1._Conta__saldo + conta2._Conta__saldo) # forma errada
print(conta1.__dict__)
conta1.limite = 700022
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)

