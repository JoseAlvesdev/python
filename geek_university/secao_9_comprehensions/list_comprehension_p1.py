"""
List Compreshension

# Exemplo numbers = [(atributo) / (loop)]
numbers = [number for number in range(0, 101)]
result = [number for number in numbers if number % 2 == 0]
print(result)

# Com uma função
def potencia(value):
    return value ** 2

numbers = [number for number in range(0, 11)]
result = [potencia(number) for number in numbers]
print(result)

# Com strings
name = 'José Henrique'
lista = [letra.upper() for letra in name]
print(lista)

# Filtrando nomes
clientes = ['jose', 'vailton', 'maria', 'mylla', 'thiago']
clientes = [cliente.title() for cliente in clientes]
print(clientes)
"""


