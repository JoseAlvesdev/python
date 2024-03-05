"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
|Python|Módulos builtin|
------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as fuções de módulo utilizando o *

from random import * # Dessa maneiro não preciso utilizar como instância
# import random

print(random())

# Utilizando alias (apelidos) para módulos/funções
from random import randint as rdi, random as rdm

print(rdi(1, 10))
print(rdm())

https://docs.python.org/3/py-modindex.html

"""
# Costumamos a utilizar tuple para colocar mútiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

lista = ['Geek', 'University', 'Python']

print(random())
print(randint(3, 7))
shuffle(lista)
print(lista)
print(choice('University'))