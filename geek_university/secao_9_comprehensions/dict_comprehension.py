"""
Dict Comprehension

# Exemplo
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: numero ** 2 for chave, numero in numeros.items()}
print(quadrado)

# Meu teste
dictio = {str(numero):numero for numero in range(0, 6)}
print(dictio)

# Outro exemplo
numeros = (numero for numero in range(1, 6))

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# Exemplo com chaves prontas GOSTEIII!
keys = ['one', 'two', 'three', 'four', 'five']
values = [numero for numero in range(1, 6)]

dicionario = {keys[i]: values[i] for i in range(0, len(keys))}

print(dicionario)

# Interessante
numeros = [numero for numero in range(0, 11)]

filter = {numero: 'par' if not numero % 2 else 'impar' for numero in numeros}

print(filter)
"""

