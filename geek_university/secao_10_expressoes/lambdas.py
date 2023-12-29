"""
Expressões lambdas

# Funcao normal
def funcao(x):
    return 3 * x + 1

# Expressao lambda
funcao = lambda x: 3 * x + 1
print(funcao(6))

# Lambda com muitas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' José ', '  Henrique   '))

# Lambda sem entradas
retorna_string = lambda: 'Como não amar python?'
print(retorna_string())

# Com lista
autores = [
    'Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 
    'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 
    'Douglas Adams', 'H. G. Wells', 'Leigh Brackett'
]

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Funcão quadrática f(x) = a* x ** 2 + b * x +c
def calcular(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

print(calcular(1, 2, 3)(2))
"""
