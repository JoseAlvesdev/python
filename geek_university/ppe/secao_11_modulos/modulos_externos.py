"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes oficiais externos em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo:

pip install <name_module>

from colorama import init
from colorama import Fore, Back, Style

init()
teste = Fore.GREEN + 'X'
teste2 = Fore.RED + 'O'

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(teste)
print(teste2)

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
"""
