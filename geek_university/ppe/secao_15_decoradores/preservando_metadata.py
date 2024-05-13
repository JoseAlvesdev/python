"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos entre arquivos

wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema


def ver_log(function):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra

        print(f'Você está chamando a {function.__name__}')
        print(f'Aqui a documentação: {function.__doc__}')

        return function(*args, **kwargs)
    return logar


@ver_log
def soma(x, y):
    # Soma dois números
    return x + y


# print(soma(1, 2))
print(soma.__name__) # soma
print(soma.__doc__) # Soma dois números


# Resolução do problema

from functools import wraps


def ver_log(function):

    @wraps(function) # Preserva os metadados das nossas funções
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra

        print(f'Você está chamando a {function.__name__}')
        print(f'Aqui a documentação: {function.__doc__}')

        return function(*args, **kwargs)
    return logar


@ver_log
def soma(x, y):
    #Soma dois números
    return x + y


# print(soma(1, 2))
print(soma.__name__) # soma
print(soma.__doc__) # Soma dois números
"""
