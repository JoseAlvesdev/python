"""
Reduce

OBS: A partir do Python3+ a função reduce () que importar e utilizar esta função a partir

Guido van Rossum: Utilize a função reduce() 99% das vezes um loop for é mais legível.

Para entender o reduce()

#Imagine que você tem uma coleção de dados:
dados (al, a2, a3, ..., an]

# E você tem uma função que recebe dois parámetros:
def funcao (x, y):
return x y
Assim como map() e filter(), a função reduce () recebe dois parámetros: a função e o iterável.

reduce (funcao, dados)

A função reduce (), funciona da seguinte forma:
    Passo 1: res1 = f(al, a2) Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3)# Aplica a função passando o resultado do passol mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)



    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce () como:

funcao (funcao (funcao (al, a2), a3), a4), ...), an)

# Exemplo
from functools import reduce

numeros = list(range(1, 11))
numeros_redux = reduce(lambda acumul, numero: acumul + numero, numeros)
print(numeros_redux)

# Ultilizando loop normal
numeros_redux = 0
for numero in numeros:
    numeros_redux += numero
    
print(numeros_redux)
"""


