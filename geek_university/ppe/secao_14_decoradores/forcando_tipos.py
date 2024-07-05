"""
Forçando tipos de dados com decoradores

zip

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)

(1, 2), (3, 4), (5, 6)

# Forçando tipo de dados

def forca_tipo(*types):
    def decorador(function):
        def converter(*args, **kwargs):
            novo_args = []
            for (value, type) in zip(args, types):
                novo_args.append(type(value))

            return function(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete(msg, vezes):
    for vez in range(vezes):
        print(msg)


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)
    

dividir('1', 5)
"""


