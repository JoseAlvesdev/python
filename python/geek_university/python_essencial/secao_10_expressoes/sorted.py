"""
Sorted

sort() so funciona pra listas, sort ele modifica a lista original.

# Exemplo
numeros = [4, 3, 2, 1, 5, 6, 7, 8]
print(sorted(numeros))

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))

# Mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": ["Eu adoro cupcake", "Eu adoro trufas"]},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu adoro meu cachorro", "Eu adoro banana", "cebola tbm"]},
    {"username": "gal", "tweets": []}
]

# Ordenando pelo username ordem alfabetica
#print(sorted(usuarios, key=lambda usuario: usuario.get('username')))

# ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario.get('tweets'))))

# Ultimo exemplo
musicas = [
    {'titulo': 'Lay Low (tiesto)', 'tocou': 10},
    {'titulo': 'In The End (tyra givens)', 'tocou': 7},
    {'titulo': 'Dragosteia (din tey)', 'tocou': 5},
    {'titulo': 'Heartless (uneverage)', 'tocou': 3},
]

# Menos tocada
print(sorted(musicas, key=lambda musica: musica.get('tocou')))

# Mais tocada
print(sorted(musicas, key=lambda musica: musica.get('tocou'), reverse=True))
"""
