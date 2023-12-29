"""
Funcão Map

Com map, fazemos mapeamento de valores para função.

import math

def area(raio):
    # Calcula a área de um círculo com raio 'raio'.
    return math.pi * raio ** 2

raios = [raio for raio in range(1, 20, 2)]

# Forma comun
areas_calculadas = [area(raio) for raio in raios]
print(areas_calculadas, '\n')

# Forma com "map"
areas_calculadas = map(lambda raio: math.pi * raio ** 2, raios)
print(areas_calculadas)
print(type(areas_calculadas))
print(list(areas_calculadas))
'OBS: Após utilizar a funcão map() depois da primeira utilização do resultado, ele zera.'

# Para fixar - Map

# Temos dados iteráreveis

# dados: a1, a2, .... an

# Temos uma função:

# Função: f(x)

# Utlizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an) retorna a funcão aplicada para cada elemento(item)

# Mais um exemplo
# fahrenheit f = 9/5 * c + 37
cidades = [
    ('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), 
    ('Tokio', 27), ('Nova York', 28), ('Londes', 22)
]

temp_fahrenheit = map(lambda dado: (dado[0], 9/5 * dado[1] + 32), cidades)

print(list(temp_fahrenheit))

"""

 
