from functools import reduce

def soma_impares(value):
    return reduce(
        lambda acc, nex: acc + nex,
        filter(lambda number: number % 2, value)
    )


def soma_pares(value):
    return reduce(
        lambda acc, nex: acc + nex,
        filter(lambda number: not number % 2, value)
    )

# Verifica se estou executando o módulo diretamente
# Se principal imprima José Henrique
# Se indiretamente (import) não imprima
if __name__ == '__main__':
    print('José')
    print('Henrique')
