curso = 'python '

print(curso.upper())

print(curso.lower())

print(curso.title())

print("--------------------------")

'''
ELIMINANDO ESPAÇOS EM BRANCO
'''

curso = "   pYtHon    "

print(curso.strip(curso.upper()))

print(curso.rstrip())

print(curso.lstrip())

print("--------------------------")

'''
JUNÇÕES E CENTRALIZAÇÃO
'''

curso = "Python"

print(curso.center(20, "-"))

print(" | ".join(curso.upper()))

