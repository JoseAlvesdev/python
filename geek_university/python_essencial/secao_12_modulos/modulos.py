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