"""
Levantando os própios erros com raise

raise -> Lança exeções

OBS: O raíse é uma função. E ua palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas exeções e menssagens de erro.

A forma geral de ultização é:

raise TipoDoErro('Menssagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Texto Texto', 'verde')

# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores:
        raise ValueError('A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('True', 'roxo')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""
# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores:
        raise ValueError('A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('True', 'roxo')