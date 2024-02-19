"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa para de funcionar e o usuário receba
mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // Execução problemática
except:
    // O que deve ser feito com caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema.')

# Tente executar a função geek(), casso você encontre erros, imprima a menssagem de erro.

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema.')

# Tente executar a função geek(), casso você encontre erros, imprima a menssagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico
    
try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro
    
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erro de uma vez.

try:
    geek()
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err:
    print(f'Deu TypeError: {err}')
except:
    print('Deu um erro diferente.')

def pega_valor(dicionario, key):
    try:
        return dicionario.get(key)
    except KeyError:
        return None
    except TypeError:
        return None
    except NameError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(teste, 'nome'))
"""

