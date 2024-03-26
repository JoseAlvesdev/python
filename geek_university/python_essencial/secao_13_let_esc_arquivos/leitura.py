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

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Mode de leitura. r -> read() -> ler (Padrão)
"""

# Exemplo

arquivo = open('texto.txt')

# print(str(arquivo))
# print(type(arquivo))

# Para ler o conteúdo de um arquivos após a sua abertura, devemos 
# utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado
# cursor. Esse cursor, funciona como o cursor quando estamos escrevendo.

# A função read() lê todo o conteúdo do arquivo.