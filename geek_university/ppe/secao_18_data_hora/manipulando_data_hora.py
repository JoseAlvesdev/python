"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente (agora)

print(datetime.datetime.now()) # 2024-07-03 08:20:25.115406 BR 03-07-2024

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajuste na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 9 horas, 0 minutos, 0 segundos, 0 microsegundo

inicio = inicio.replace(year=2023, hour=9, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data

print(type(evento))

print(type('31/12/2024'))

print(evento)

nascimento = input('Informe sua data de nascimento [dd/mm/yyyy]: ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year) # Ano
print(evento.month) # Mês
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.microsecond) # Microsegundo

print(dir(evento))