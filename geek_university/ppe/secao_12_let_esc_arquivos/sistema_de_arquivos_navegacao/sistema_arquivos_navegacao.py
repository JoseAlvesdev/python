"""
Sistema de Arquivos e Navegação

Para fazer uso de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Fazer o import

import os

# getcwd() -> pega o current work direcory - diretório de trabalho 
# corrente

# Retorna o path (caminho) absoluto

print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório e absoluto ou relativo

print(os.path.isabs('/Documents/Estudos/python/python')) # True

# OBS para usuários windows 
# Se você, infelizmente estiver utilizando um computador windows
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\joseh'))

# Podemos indentificar o Sistema Operacional com o módulo os

print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no Sistema operacional

#print(os.uname()) # (Linux) Não funciona no windows

import sys

print(sys.platform)

# Juntando diretórios

print(os.getcwd()) # C:\Users\joseh\Documents\Estudos\python

res = os.path.join(os.getcwd(), 'python', 'geek_university')

os.chdir(res)

print(os.getcwd())
# C:\Users\joseh\Documents\Estudos\python\python\geek_university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro
# o diretório atual e o segundo o diretório que vc quer caminhar (chegar)
# ou juntar ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir()) # len()
# Posso passar paths para a leitura
"""
# Fazer o import

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
scammer = os.scandir('./')

arquivos = list(scammer)
#print(arquivos)

#print(dir(arquivos[0]))

print(arquivos[0].name) # Nome do arquivo

print(arquivos[0].inode()) # ?

print(arquivos[0].is_dir()) # É um diretório? 

print(arquivos[0].is_file()) # É um arquivo?

print(arquivos[0].is_symlink()) # É um link simbólico?

print(arquivos[0].path) # path (caminho)

print(arquivos[0].stat()) # Estátisticas

# Quando utilizamos a função scamdir() nós precisamos fecha-la. 
# assim quando abrimos um arquivo.

scammer.close()