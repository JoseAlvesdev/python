"""
List Comprehension

numeros = [numero for numero in range(1, 11)]

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 e 1, e 1 em python e True.
impares = [numero for numero in numeros if numero % 2]

# Esta pegando os numeros pares e multiplicando * 2 e dividinho os impares / 2.
result = [numero * 2 if not numero % 2 else numero / 2 for numero in numeros]
"""

