"""
Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiane', 'José']

# Usando list comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res)); print(res, '\n')

# Usando generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res)); print(tuple(res))

# Qual e a utilidade getsizeof()? Retorna a quantidade de bytes em memória do elemento passado por parametro.
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memoria. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'), 'bytes')
print(getsizeof('University'), 'bytes')
print(getsizeof('Geek'), 'bytes')

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([numero*10 for numero in range(1, 1000)])

# Gerando uma conjunto de numeros com Set Comprehension
set_comp = getsizeof({numero*10 for numero in range(1, 1000)})

# Gerando um dicionario de numeros com dict Comprehension
dict_comp = getsizeof({f'{numero}*10': numero*10 for numero in range(1, 1000)})

# Gerando uma lista de numeros com List Comprehension
generator_comp = getsizeof(numero*10 for numero in range(1, 1000))

qtd_bytes = [list_comp, set_comp, dict_comp, generator_comp]

print(tuple((print(f'Tamanho: {byte}bts') for byte in qtd_bytes)))
"""
gen = (x * 10 for x in range(1000))
for x in gen: print(x)