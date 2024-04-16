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
"""
import os

# Renomear arquivos e diretórios