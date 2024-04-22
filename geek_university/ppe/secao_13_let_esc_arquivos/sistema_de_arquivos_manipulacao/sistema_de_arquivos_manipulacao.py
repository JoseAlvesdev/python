"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretoria existe

# Paths relativos (Relativo ao diretório que estou)
# Arquivo
print(os.path.exists('sistema_de_arquivos_manipulacao.py')) # True


# Diretório
print(os.path.exists('scripts')) # False

# Paths absolutos
print(os.path.exists('../sistema_de_arquivos_manipulacao'), '->') # True
print(os.path.exists('../scripts')) # False
print(os.path.exists('../escrita.py../get-pip.py')) # False

# Criando arquivos

# Forma 1
open('novo.txt', 'x').close()

# Forma 2
open('nov2.txt', 'a').close()

# Forma 3
open('novo3.txt', 'w').close()

# Forma 4
with open('novo4.txt', 'x'):
    pass
    
# Criando arquivos

# os.mknod('novo.txt') # Não funciona no Windows
# os.mkfifo('novo.txt') # Não funciona no Windows

# OBS: Se você estiver usando no MacOS, pode haver um erro de PermissionError

# OSB: Criando um arquivo via mknod() se o arquivo já existir teremos o
# erro FileExitsError

# Criando diretórios - únicos (um a um)

# os.mkdir('templates')

# os.mkdir('templates/geek/university')

# os.mkdir('templates/geek/university')

# Path Relativo
os.mkdir('novo')

# Path Absoluto

os.mkdir('./ppe/secao_13_let_esc_arquivos/sistema_de_arquivos_manipulacao/novo')

# OSB: Criando um diretório via mkdir() se o diretório já existir teremos o
# erro FileExitsError

os.mkdir('/etc/templates')

# OBS: Se não tivermos permisão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)

os.makedirs('templates/geek/university')

# Se já existir, teremos um FileExistsError

os.makedirs('templates/geek/university', exist_ok=True)

# Se existir ignore exist_ok=True

# Renomear diretórios

os.mkdir('novo')
os.rename('novo', 'new')

# OBS.: Se o diretório não existir teremos um FileNotFoundError

# OSB.: Se o diretório que queremos renomear não estiver vazio, teremos um
# OSError

# Renomear arquivos

with open('novo.txt', 'x'):
    pass

os.rename('novo.txt', 'new.txt')
os.rename(
    'C:\\Users\\joseh\\OneDrive\\Área de Trabalho\\new.txt', 
    'C:\\Users\\joseh\\OneDrive\\Área de Trabalho\\bosta-d-mierda.txt'
    # Passar o caminho inteiro
)

# Removendo arquivos (não remove diretórios)

# Atenção tome cuidado com os comando de deleção. Ao deletarmos um arquivo
# não vão para a lixeira. São deletados permanentemente.

open('novo.txt', 'x').close()
sleep(5)
os.remove('novo.txt')

# OBS: Se você estiver no windows e o que você for deletar estiver em uso,
# você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um
# IsADirectoryError

# Removendo diretórios vazios

os.mkdir('novo')
sleep(5)
os.rmdir('novo')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OSB: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretorios

for arquivo in os.scandir('novo'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    # else:
    #     os.rmdir(arquivo.path)
    #     # So se estiver vazio

# Podemos remover um árvore de diretórios vazio

os.makedirs('novo/novo2/novo3/novo6', exist_ok=True); sleep(5)
os.removedirs('novo/novo2/novo3/novo6')

# Se algum dos diretórios contiver arquivos ou outros diretórios o processo
# é interrompido

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a
# lixeira. Eles são excluidos permanentemente.

# pip install send2trash (manda pra lixeira)

sudo apt-get install lsb-core

# Enviando arquivos e diretórios para a lixeira
open('novo.txt', 'x').close()
open('new.txt', 'x').close(); sleep(5)

os.remove('novo.txt') # Não vai para a lixeira (deletado permanentemente)
remove('new.txt') # Vai para a lixeira

# OBS: Se o arquivo não existir teremos OSError (send2trash)

os.mkdir('novo'); sleep(5)
remove('novo')

# Trabalhando com arquivos e diretórios temporários

with tempfile.TemporaryDirectory() as temp:
    print(f'Criei o diretório temporário em {temp}')

    with open(os.path.join(temp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
        input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele
# criando um arquivo escrevemos um texto. No final, usamos um input() só
# para mantermos os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver
# utilizando o windows. Por conta desse sistema trabalhar de forma 
# diferente com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as temp:
    temp.write(b'Geek University\n') # b dados binários
    temp.seek(0)
    print(temp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, 
# utilizamos b'string'

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

============

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

imports utilizados

import os
import tempfile
from send2trash import send2trash as remove
from time import sleep

https://docs.python.org/3/library/os.html?highlight=os#module.os

documentação do módulos OS
"""


