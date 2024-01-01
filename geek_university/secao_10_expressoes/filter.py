"""
Filter

filter() -> Server para filtrar dados de ma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

# OBS.: Assim com a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável
res = filter(lambda x: x > media, dados)
print(list(res))
print(list(res)) # OBS:. Assim como no map(), os dados são excluidos da memoria após a primeira utilização

paises = ['', 'Argentina', '', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', 'Venezuela', '', '']

# paises_filtrados = filter(lambda pais: pais, paises)
paises_filtrados = filter(None, paises)
print(list(paises_filtrados))

# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato", "Eu adoro chocolate"]},
    {"username": "jeff", "tweets": ["Eu adoro cupcake", "Eu adoro trufas"]},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu adoro meu cachorro", "Eu adoro banana"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter
users_inativos = filter(lambda usuario: not usuario.get('tweets'), usuarios)
print(list(users_inativos))

# Combinar filter() map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutrura é' + nome, desde que cada nome tenha menos de 5 caracteres
nomes_modificados = list(map(lambda nome: f'Sua instrutrura é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(nomes_modificados)
"""

