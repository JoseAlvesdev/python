"""
Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos

Pacote -> É um diretório uma coleção de módulos:

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um 
arquivo chamado __init__.py

Nas versões do Python 3.x nãoe é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizado para mater compatibilidade.

from geek import geek1, geek2

# Importando um Sub Pacote com seus módulos
from geek.university import geek3, geek4

print(geek1.PI)

print(geek1.funcao1(4, 6))

print(geek2.CURSO)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())


"""
from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(5, 5))

print(funcao4())