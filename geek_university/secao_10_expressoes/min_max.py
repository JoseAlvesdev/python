"""
Min e Max

max() -> Retorna os valores máximos de um ou mais elementos.

# Exemplos

# Lista
numeros = [1, 2, 3, 7, 8, 9, 99, 55, 130]
print(max(numeros))

# Tupla
numeros = (1, 2, 3, 7, 8, 9, 99, 55, 130)
print(max(numeros))

# Set
numeros = {1, 2, 3, 7, 8, 9, 99, 55, 130}
print(max(numeros))

# Dict
'values(), keys()'
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 7, 'e': 8, 'f': 9, 'g': 99, 'h': 55, 'i': 130}
print(max(numeros.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior
valores = input().split()
print(max(valores))

# Exemplos
print(max('a', 'ab', 'abc')) # Três valores
print(max('a', 'b', 'c', 'g')) # Quatro valores
print(max(1, 2, 3, 4, 5, 6, 7, 8)) # Oito valores
print(max('José Henrique'))

# Lista
numeros = [1, 2, 3, 7, 8, 9, 99, 55, 130]
print(min(numeros))

# Tupla
numeros = (1, 2, 3, 7, 8, 9, 99, 55, 130)
print(min(numeros))

# Set
numeros = {1, 2, 3, 7, 8, 9, 99, 55, 130}
print(min(numeros))

# Dict
'values(), keys()'
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 7, 'e': 8, 'f': 9, 'g': 99, 'h': 55, 'i': 130}
print(min(numeros.values()))

# Faça um programa que receba dois valores do usuário e mostre o menor
valores = input().split()
print(min(valores))

# Exemplos
print(min('a', 'ab', 'abc')) # Três valores
print(min('a', 'b', 'c', 'g')) # Quatro valores
print(min(1, 2, 3, 4, 5, 6, 7, 8)) # Oito valores
print(min('Jose Henrique'), 'essa')

# Outros exemplos

nomes = ['Arya', 'Samson', 'José', 'Tim', 'Olivander']

# Por padrão ele imprime o menor valor em ordem alfabetica.
print(min(nomes)) # Arya
print(max(nomes)) # Tim

# Alterando a funcão.
print(min(nomes, key=lambda nome: len(nome)))
print(max(nomes, key=lambda nome: len(nome)))

musicas = [
    {'titulo': 'Lay Low (tiesto)', 'tocou': 10},
    {'titulo': 'In The End (tyra givens)', 'tocou': 7},
    {'titulo': 'Dragosteia (din tey)', 'tocou': 5},
    {'titulo': 'Heartless (uneverage)', 'tocou': 3},
]

print(max(musicas, key=lambda musica: musica.get('tocou')))
print(min(musicas, key=lambda musica: musica.get('tocou')))

# DESAFIO! Imprima somente o titulo da música mais e menos tocada.

print(max(musicas, key=lambda musica: musica.get('tocou')).get('titulo'))
print(min(musicas, key=lambda musica: musica.get('tocou')).get('titulo'))

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar 
# max(), min() e lambda?
max = 0

for musica in musicas:
    max = musica.get('tocou') if musica.get('tocou') > max else max
    mais_tocada = musica.get('titulo') if musica.get('tocou') == max else mais_tocada

print(mais_tocada)

min = 999999

for musica in musicas:
    min = musica.get('tocou') if musica.get('tocou') < min else min
    mais_tocada = musica.get('titulo') if musica.get('tocou') == min else mais_tocada

print(mais_tocada)
"""
