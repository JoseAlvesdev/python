"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

"Geek", "University", "Python", "Ciência", "Dados"

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"Geek"; "University"; "Python"; "Ciência"; "Dados"

# Separador por espaço

1 2 3 4 5 6

"Geek" "University" "Python" "Ciência" "Dados"

OBS.: Dica do professor manter um padrão de separadores, usar um só.

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('./recursos/lutadores.csv', encoding='UTF-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas de diferentes para ler dados em arquivos CSV:
    - reader -> Permite que itremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts

# Reader

from csv import reader

with open('./recursos/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular cabecalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader

from csv import DictReader

with open('./recursos/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(linha)
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
"""

# DictReader com outro separador

from csv import DictReader

with open('./recursos/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        # print(linha)
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")