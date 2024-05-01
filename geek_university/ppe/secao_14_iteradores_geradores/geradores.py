"""
Geradores
    - Geradores (Generators) são Iterators (Iteradores):

OBS: O contrário não é verdadeiro, Ou seja, nem todo iterator é um generator.

Outras informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;

Diferença entre Funções e Generator Functions (Funções Geradoras)

========================================================================
|| Funções                       || Generator Functions               ||
========================================================================
|| utilizam return               || utilizam yield                    ||
========================================================================
|| Retorna uma vez               || podem utilizar yeld multiplas vezes ||
========================================================================
|| quando executada, retorna um valor || quando executada, retorna um generator ||
========================================================================

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for i in gen:
    print(i)

gen = conta_ate(10) # 1

print(next(gen))

print('->')

for num in gen:
    print(num)

# Exemplo Generator Function (Função Geradora)

def conta_ate(valor_maximo):
    contador = 1
    
    while contador <= valor_maximo:
        yield contador
        contador += 1


# Uma Generator function não é um Generator, ele gera um generator, ok?

gen = list(conta_ate(10))

print(gen)    
"""
