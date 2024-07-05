"""
zip() -> Cria um iterável (zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

# Exemplos

numeros = list(range(1, 4)) # [1, 2, 3]
numeros2 = list(range(4, 7)) # [4, 5, 6]

zip1 = zip(numeros, numeros2)

print(type(zip1))

# Sempre podemos gerar uma lista, tupla, conjunto ou dicionario.

print(list(zip1))

zip1 = zip(numeros, numeros2)
print(tuple(zip1))

zip1 = zip(numeros, numeros2)
print(set(zip1))

zip1 = zip(numeros, numeros2)
print(dict(zip1))

# OBS.: O zip utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver
# trabalhando como iteráveis de tamanhos diferentes, irá parar quando os elementos do menor
# iterável acabar

numeros3 = list(range(7, 12)) # [7, 8, 9, 10, 11]

zip1 = zip(numeros, numeros2, numeros3)

print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = tuple(range(1, 6))
lista = list(range(6, 11))
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

# Exemplos mais complexos

prova1 = [80, 91, 18]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# final = {dado[2]: max(dado[0], dado[1]) for dado in zip(prova1, prova2, alunos)}

# print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
"""
