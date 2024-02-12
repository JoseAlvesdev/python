"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRA DO USUÁRIO DEVE SER TRATADA!

OBS: A função do usuário e DESTRUIR seu sistema

# Else -> É executado somente se não ocorrer o erro.

num = False

while True:
    try:
        num = int(input('Digite um valor: ')) 
    except ValueError:
        print('Valor incorreto.')
    else:
        print(f'Você digitou {num}') 

    if num: break

# Finally

try:
    num = int(input('Digite um valor: '))
except ValueError:
    print('Você não digitou um número.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executado o finally')

# OBS: O bloco finally é sempre executado. Independente se houve exeção ou não.
    
# O finally, geralmente é utlilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(num_1, num_2):
    return num_1 / num_2

try:
    num_1, num_2 = int(input()), int(input())
except ValueError:
    print('O valor digitado não é número!')
else:
    print(dividir(num_1, num_2))
finally:
    print('Tratamento finalizado.')

# Exemplo mais complexo CORRETO
# OBS: Você e reponsável pela entrada das suas funções. trate-as!

def dividir(num_1, num_2):
    try:
        return num_1 / num_2
    except ValueError:
        return 'Valor incorreto.'
    except TypeError:
        return 'Tipo incorreto'
    except ZeroDivisionError:
        return 'Não e possível dividir por zero.'
  

print(dividir(3, 3))

# Exemplo mais complexo - GENÉRICO
# OBS: Você e reponsável pela entrada das suas funções. trate-as!

def dividir(num_1, num_2):
    try:
        return num_1 / num_2
    except:
        return 'Algo deu errado.'


print(dividir(3, []))

# Exemplo mais complexo - Semi GENÉRICO
# OBS: Você e reponsável pela entrada das suas funções. trate-as!

def dividir(num_1, num_2):
    try:
        return num_1 / num_2
    except (TypeError, ZeroDivisionError) as err:
        return f'Algo deu errado: {err}.'


print(dividir(3, '2'))
"""
