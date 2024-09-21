"""
Tipo string

Em Python um dado e considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Sempre que estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Ginas'Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# nome = [triplas]"Angelina 
# Jolie" # Quebra a linha
# nome = "Angelina \"Jolie\"" # Consigo imprimir aspas duplas dentro de aspas duplas
# print(nome)
# print(type(nome))

# ================================
# MÉTODOS DE STRING

# UPPER
print(nome.upper())

# LOWER
print(nome.lower())

# SPLIT
print(nome.split()) # Transforma em uma lista de strings
# [ 0,   1,   2,   3,   ...]
# ['G', 'e', 'e', 'k', ' ', ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print(nome[0:4]) # slice de string
print(nome[5:15]) # slice de string

# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
nome = 'Geek University'

# [::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e iverta.
print(nome[::-1]) # Inversão da String Pythonico

print(nome.replace('e', 'i'))

# TEXTOS PALINDROMOS KKK
texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])

nome = 'ana'
print(nome)

print(nome[::-1])