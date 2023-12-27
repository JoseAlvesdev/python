"""
Set Comprehension
"""

numeros = {numero for numero in range(0, 11)}
keys = ['pares', 'impares']

filter = {
    keys[0]: {numero for numero in numeros if not numero % 2}, 
    keys[1]: {numero for numero in numeros if numero % 2}
}


conjunto = {1, '2', 3, 4, '2', '3', 5, 6, 6, '9'}
print(conjunto) # {1, 3, 4, 5, 6, '2', '3'}
