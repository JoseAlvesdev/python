"""
Modos de ASbertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve uma arquivo já existente
x -> Abre para escrita somente se o arquivo não existir.
a -> Abre para escrita, adiconando o conteúdo ao final do arquivo SEMPRE.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o contro
le do cursor)

# OBS: Abrindo no modo 'a' -> append, se o arquivo existir será criado.
Caso exista, o novo conteúdo será adicionado ao final. Com o modo a não
controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

# Exemplo x

with open('novo.txt', 'w') as arquivo:
    i = 0
    while i < 4:
        arquivo.write(f'-> {i}\n')
        i += 1

try:
    with open('novo.txt', 'x') as arquivo:
        i = 0
        while i < 4:
            arquivo.write(f'-> {i}\n')
            i += 1
except FileExistsError:
    print('Arquivo já existe')

# Exemplo a

with open('novo.txt', 'w') as arquivo:
    i = 0
    while i < 4:
        arquivo.write(f'-> {i}\n')
        i += 1

with open('novo.txt', 'a') as arquivo:
    i = 0
    while i < 4:
        arquivo.write(f'-> {i}\n')
        i += 1

# Exemplo r+
with open('novo.txt', 'r+') as arquivo:
    i = 0
    while i < 4:
        arquivo.write(f'-> {i}\n')
        i += 1
"""
