"""
Decorators com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto Decorator Pattern

# Relembrando

def gritar(function):
    def aumentar(nome):
        return function(nome).upper()
    
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o (a) {nome}'

@gritar
def ordernar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento} por favor.'


# Testando

# print(saudacao('Angelina'))

print(ordernar('Picanha', 'Queijo'))


A assinatura de uma função é representado pelo seu retorno, nome e parâmetros
de entrada.

# Refatorando com a Decorator Pattern


def gritar(function):
    def aumentar(*args, **kwargs):
        return function(*args, **kwargs).upper()
    
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o (a) {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento} por favor.'


@gritar
def lol():
    return 'lol'


print(saudacao('Angelina'))
print(ordernar('Picanha', 'Queijo'))
print(lol())

# OBS: Vale lembrar que podemos utilizar parâmentros nomeados.

print(ordernar(principal='Picanha', acompanhamento='Queijo'))

# Decorator com argumentos

def verifica_primeiro_argumento(value):
    def interna(function):
        def outra(*args, **kwargs):
            if args and args[0] != value:
                return f'Valor incorreto! Primeiro argumento precisa ser {value}'
            
            return function(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(nb1, nb2):
    return nb1 + nb2

# Testando

print(comida_favorita('pizza'))
print(soma_dez(10, 5))
"""

# Decorator com argumentos

"""
EXEMPLO JULIO GRUPO DE PYTHON TELEGRAM

def nunca(func):
    def inner(*args, **kwargs):
        print('NÃO! FUNÇÃO É PROÍBIDA DE SER CHAMADA!')
        return ""
    return inner


def saudacao(nome):
    return f'Olá {nome}'


@nunca
def hello(nome):
    return f'Hello {nome}'


print(saudacao('Julio'))
print(hello('José'))
"""