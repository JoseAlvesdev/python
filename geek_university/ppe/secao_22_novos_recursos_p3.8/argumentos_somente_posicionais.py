"""
Argumentos Somente Posicionais

def start(Tudo antes da barra dever ser posiconal /):
    pass
    

def start_v2(*, tudo depois do asterisco deve ser informando o parametro):
    pass

"""

# valor = '67.3'
# print(float(valor))


# def cumprimenta_v1(nome):
#     return f'Olá {nome}'


# print(cumprimenta_v1('Geek'))
# print(cumprimenta_v1(nome='Geek'))


# def cumprimenta_v2(nome, /):
#     return f'Olá {nome}'


# print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))


# def cumprimenta_v3(nome, /, mensagem='Olá'):
#     return f'{mensagem} {nome}'


# print(cumprimenta_v3('Geek'))
# print(cumprimenta_v3('University', mensagem='Hello'))
# print(cumprimenta_v3('Felicity', 'Bem-vinda'))

# def cumprimenta_v4(nome, menssagem='Olá', /):
#     return f'{menssagem} {nome}'

# print(cumprimenta_v4('Geek'))
# print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('University', menssagem='Hello'))

# ==============================
# Parametros somente nomeados
# ==============================


# def cumprimenta_v5(*, nome):
#     return f'Olá {nome}'


# print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))


def cumprimentar_v6(nome, /, menssagem_1='Olá', *, menssagem_2):
    return f'{menssagem_1} {nome} {menssagem_2}'


print(cumprimentar_v6('Geek', menssagem_1='Hello', menssagem_2='tenha um bom dia'))
print(cumprimentar_v6('Geek', menssagem_2='tenha um bom dia'))
print(cumprimentar_v6('Geek', 'oi', menssagem_2='Vamos?'))