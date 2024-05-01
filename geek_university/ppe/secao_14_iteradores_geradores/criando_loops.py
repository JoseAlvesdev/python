"""
Criando a minha própia versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Geek University')

# Meu Loop

def meu_for(iterable):
    it = iter(iterable)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros =  list(range(1, 5 + 1))

meu_for(numeros)
"""
