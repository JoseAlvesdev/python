"""
Peça o usuário para digitar três valores inteiros e imprima a soma deles.
"""

numbers = []; numbers.extend((input('Digite 3 números inteiros: ').split()))
numbers = [int(number) for number in numbers]
soma = 0

for number in numbers:
    soma += number

print(f'soma = {soma}')