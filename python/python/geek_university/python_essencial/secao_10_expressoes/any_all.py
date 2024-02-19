"""
Any e All

all() > Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exmeplo all()
print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiro? False
print(all([1, 2, 3, 41])) # Todos os números são verdadeiro? True
print(all('')) # Todos os números são verdadeiro? True
print(all([])) # Todos os números são verdadeiro? True
print(all((1, 2, 3, 41))) # Todos os números são verdadeiro? True
print(all({1, 2, 3, 41})) # Todos os números são verdadeiro? True
print(all('Geek')) # Todos os números são verdadeiro? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiane', 'José']
# print(nomes[4][2]) # i
print(all(nome[0] == 'C' for nome in nomes))

# OBS: Um iteráel vazio convertidjo em boolean é False, mas o all() entende com True
print(all([letra for letra in 'aio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if not num % 2]))
all() = todos
any() = algum

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 3, 4])) # True # bastar ter um elemento verdadeiro que any() retorn True

print(any([0, False, [], {}, 1])) # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiane', 'José']
print(any(nome[0] == 'C' for nome in nomes)) # True

print(any([numero for numero in list(range(0, 11)) if not numero % 2])) # True
"""
