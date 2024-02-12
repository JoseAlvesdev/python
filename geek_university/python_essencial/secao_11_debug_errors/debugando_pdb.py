"""
Debugando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inset

# OBS: A utilização do print() para debugar código e um prática ruim.

def dividir(n1, n2):
    try:
        return int(n1) / int(n2)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utlizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o pyCharm ou utlizando
# o PDB - Python Debugger

# Exemplo com o PyCharm

def dividir(n1, n2):
    try:
        return int(n1) / int(n2)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    

print(dividir(4, 0))

# Exemplo com o PDB Debugger 1
# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utlizar a funcão set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - Finaliza o debugging)
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = f'{nome} {sobrenome}'
curso = 'Programação em Python: Essencial'
final = f'{nome_completo} faz o curso de {curso}'
print(final)

# Exemplo com o PDB Debugger 2
# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utlizar a funcão set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - Finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = f'{nome} {sobrenome}'
curso = 'Programação em Python: Essencial'
final = f'{nome_completo} faz o curso de {curso}'
print(final)

# Por que utilizar este formato?
# O debug é utlizado durante o desenvolvimento. Custumamos realizar todos os imports de biblioteca
# no inicio do arquivo. Por isso, ao invés de colocarmos os import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo com o PDB Debugger 3
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utlizar a funcão set_trace()

# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb pois comando de debug foi imcorporado como função builtin (integrada) chamada "breakpoint()"

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável) comando -> p (l) variavel
# c (continua a execução - Finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = f'{nome} {sobrenome}'
curso = 'Programação em Python: Essencial'
final = f'{nome_completo} faz o curso de {curso}'
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
"""
