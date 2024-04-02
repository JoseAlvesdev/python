"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional
precisa ter permissão:
    - Permisão de Leitura -> Para ler o arquivo.
    - Permisão de Escrita -> Para escrever no arquivo.

StringIO -> Utilizado para ler ou criar arquivos em memória.

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo em mémoria já com uma string inserida ou 
# mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)
# with open('arquivo.txt', 'w') as arquivo: (equivalente)

# Agora tendo o arquivo podemos utilizar tudo o que já sabemos
print(arquivo.read())

# Escreva outros textos
arquivo.write('Novo texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())

print(arquivo.closed)

arquivo.close()

print(arquivo.closed)
"""

