"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a funcão 
integrada open(), que literalmente significa 'abrir'.

open() -> A forma mais simples de de utilização nos passamos apenas um 
parâmetro de entrada, que neste caso é o caminho para o arquivo a ser 
lido. Essa função retorna um _io.TextIOWrapper e é com ele que 
trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. 
Este arquivo deve existir, ou então teremos o erro FileNotFoundError.
"""

# Exemplo

arquivo = open('texto.txt')

print(arquivo, type(arquivo))