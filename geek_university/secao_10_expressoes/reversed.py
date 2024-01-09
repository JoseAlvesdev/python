"""
Reversed

OBS: Não confundir com a função reverse() das listas

Já a função reversed() funciona com qualquer iterável list, tuple, dict, set.

A função reversed() retorna um iterável chamado List Reverse Iterator

# Exemplos
lista = list(range(1, 6))

# Podemos converter o elementor retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
# OBS.: Em conjuntos não definimos a orderm dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))
#print(list(reversed('Geek University')))

# Já vimos como fazer isso de forma mais fácil com o slice de strings
print('Geek University'[::-1])

# Apesar que tbm já vimos como fazer isso utilizando o própio range()
numeros = list(range(10, 0, -1))

print(numeros)
"""

