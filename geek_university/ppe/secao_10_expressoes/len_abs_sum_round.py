"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável

# Len
print(len('Geek University'))

print(len(list(range(1, 6))))

print(len(tuple(range(1, 6))))

print(len(set(range(1, 6))))

keys = ['a', 'b', 'c', 'd', 'e']
print({key: len(keys) for key in keys})

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte

# Dunder len
print('Geek University'.__len__())

#Abs

abs() -> retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos
# Praticamente deixa um número positivo (valor absoluto)
# Não funciona com strings

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
print(abs('Geek'))

#sum()

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial

# Exemplos sum
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], -5))

print(sum([3.145, 5.678]))
print(sum((3.145, 5.678)))
print(sum({3.145, 5.678}))
print(sum({'valor': 10, 'valor_2': 10}.values()))

# OBS:l O valor inicial defalt = 0

# Round

round() -> Retorna um número arredondado para n dígitos de precisão após a casa decimal. Se a precisão não for informada retorna o inteiro mas próximo da entrada

# Exemplos round

print(round(3.49))
print(round(3.50))
print(round(3.51))

print(round(1.2121212121, 3))
print(round(1.21999999, 2))
"""

