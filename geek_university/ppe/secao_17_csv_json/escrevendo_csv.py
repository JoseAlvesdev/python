"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
# Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])

    while filme != 'sair':
        filme = input('Nome do filme: ')

        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter

# OBS: As chaves do dicionário devem ser as mesma utilizadas no cabecalho

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow({cabecalho[0]: filme, cabecalho[1]: genero, cabecalho[2]: duracao})
