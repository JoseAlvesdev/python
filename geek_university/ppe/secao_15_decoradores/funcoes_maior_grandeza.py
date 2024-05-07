"""
Funcões de Maior Grandeza - Highler Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação supoprte HOF, indica podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar varáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(value, value_2, function):
    return function(value, value_2)


# Testando as funções

print(calcular(2, 5, somar))
print(calcular(2, 5, subtrair))
print(calcular(2, 5, multiplicar))
print(calcular(2, 5, dividir))

# Nested Functions - Funções Aninhadas

# Em python podemos também ter funções dentro de funções, que são conhecidas
# por Nested Functions ou também Inner Functions (Funções Internas).

# Exemplo

from random import choice

def cumprimento(pessoa):

    def humor():
        return choice(('E aí ', 'Tá doidão? ', 'Tu é gente boa ',))
    
    return humor() + pessoa


print(cumprimento('José'))

# Retornando funções de outras funções

from random import choice

def faca_me_rir():
    
    def rir():
        return choice(('kkkkkkk', 'hahahahaha', 'hehehehe',))
    
    return rir

# Testando

rindo = faca_me_rir()

print(rindo())

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo
# de funções mais externas.

from random import choice

def faca_me_rir_novamente(pessoa):

    def rindo():
        risada = choice(('hahahahaha', 'hehehehehe', 'kkkkkkkkkk',))
        return f'{risada} {pessoa}'
    
    return rindo


# Testando

rindo = faca_me_rir_novamente('José')

print(rindo())
"""


