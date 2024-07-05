"""
Teste de Velocidade com Expressões Geradoras

# Generators (Geradores)

def nums():
    for num in range(1, 9 + 1):
        yield num


gen1 = nums()

print(gen1) # Generator
print(next(gen1))

# Generator Expression

gen2 = (num for num in range(1, 9 + 1))

print(gen2) # Generator Expression
print(next(gen2))


# Realizando o teste de velocidade.
import time

# Generator Expression
# Generator Expression levou 69.76449513435364
gen_inicio = time.time()
print(sum(num for num in range(1000000000))) # 10 bilhões
gen_tempo = time.time() - gen_inicio

# List Comprehension
# List Comprehension levou 300.81707859039307
list_inicio = time.time()
print(sum([num for num in range(1000000000)])) # 10 bilhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
"""
