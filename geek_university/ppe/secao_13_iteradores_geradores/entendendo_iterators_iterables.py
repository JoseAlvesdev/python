"""
Entendendo Iterators e Iterables


Iterator -> 
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma
    função next() é chamada:

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for
    chamada.

    (Antes de eu transformar um Iterator ele é um Iterable)


nome = 'Geek' # É um iterable más não é um iterator.

# É um iterable más não é um iterator.
numeros = [number for number in range(1, 10 + 1)]

# Transformando-os em iterator
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))

nome = 'Geek'

#for [Iterator] in [Iterable]:
    #print(next(Iterator))

for letra in nome:
    print(letra)
"""

