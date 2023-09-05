numeros = [1, 2, 4, 6, 5, 56, 0, 7, 3]
pares = []
quadrado = []

'''
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
'''

'''
    for numero in numero:
        quadrado.append(numero ** 2)
'''

pares = [numero for numero in numeros if numero % 2 == 0]

quadrado = [numero ** 2 for numero in numeros]

print(pares[::])
print(quadrado[::])