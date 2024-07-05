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
"""

import datetime


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

hoje_formatado = hoje.strftime('%d de %B de %Y')

print(hoje_formatado)
