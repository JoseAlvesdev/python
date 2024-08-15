"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now() # now == agora
print(agora, type(agora), repr(agora), sep='\n')

hoje = datetime.datetime.today() # today == hoje
print(hoje, type(hoje), repr(hoje), sep='\n')

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time()) # time() zera as horas
print(manutencao, type(manutencao), repr(manutencao), sep='\n')

# Econtrar o dia da semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sanday)

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento [dd/mm/yyyy]: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

print(aniversario)

match aniversario.weekday():
    case 0:
        print('Você nasceu em uma segunda-feira.')
    case 1:
        print('Você nasceu em uma Terça-feira.')
    case 2:
        print('Você nasceu em uma Quarta-feira.')
    case 3:
        print('Você nasceu em uma Quinta-feira.')
    case 4:
        print('Você nasceu em uma Sexta-feira.')
    case 5:
        print('Você nasceu em uma Sábado.')
    case 6:
        print('Você nasceu em uma Domingo.')

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

# ANO
# y minúsculo mostra o ano somente com 2 dígitos

# MÊS
# B maiúsculo mostra o nome do mês em inglês
# b minúsculo mostra as 3 primeiras letras iniciais do mês

# Consultar: https://docs.python.org/3/library/datetime.html

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

def formata_data(data):

    match data.month:
        case 1:
            return f'{data.day} de Janeiro de {data.year}'
        case 2:
            return f'{data.day} de Fevereiro de {data.year}'
        case 3:
            return f'{data.day} de Março de {data.year}'
        case 4:
            return f'{data.day} de Abril de {data.year}'
        case 5:
            return f'{data.day} de Maio de {data.year}'
        case 6:
            return f'{data.day} de Junho de {data.year}'
        case 7:
            return f'{data.day} de Julho de {data.year}'
        case 8:
            return f'{data.day} de Agosto de {data.year}'
        case 9:
            return f'{data.day} de Setembro de {data.year}'
        case 10:
            return f'{data.day} de Outubro de {data.year}'
        case 11:
            return f'{data.day} de Novembro de {data.year}'
        case 12:
            return f'{data.day} de Dezembro de {data.year}'

# Função refatorada.

import datetime
from deep_translator import GoogleTranslator


def formata_data(data):
    return f"{data.day} de {GoogleTranslator(target='pt').translate(data.strftime('%B'))} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))

nascimento = datetime.datetime.strptime('11/05/2000', '%d/%m/%Y')

print(nascimento)

# Pegando uma string informada pelo usuário, e convertendo em um datetime
# com o método strptime()

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))