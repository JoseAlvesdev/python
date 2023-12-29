"""
Set Comprehension

# Meu exemplo
numeros = {numero for numero in range(0, 11)}
keys = ['pares', 'impares']

filter = {
    keys[0]: {numero for numero in numeros if not numero % 2}, 
    keys[1]: {numero for numero in numeros if numero % 2}
}

# Exemplos
numeros = set(range(1, 11))
print(numeros)

numeros = {num ** 2 for num in range(10)}
print(numeros)

# DESAFIO! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set.

numeros = {'numeros': {num ** 2 for num in range(10)}}
print(numeros)

# DESAFIO!
letras = {letra for letra in 'Geek University'}
print(letras)
"""
