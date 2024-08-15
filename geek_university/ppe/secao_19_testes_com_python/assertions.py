"""
Assertions (Afimações/checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma espressão que queremos checar se é válida]
ou não.
Se a expresão for verdadeira, retorna None e caso seja falsa levanta um erro

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo
uma menssagem de erro personalizada;

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...
não precisa ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion
será validado. Ou seja, todas as suas validações já eram.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos.'
    return a + b


print(soma_numeros_positivos(4, 2)) # 6
print(soma_numeros_positivos(-1, 2)) # AssertionError

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


print(comer_fast_food(input('Informe a comida: ')))

# ALERTA: Cuidado ao utilizar 'assert'


def destroi_todo_sistema():
    pass

def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins!'
    destroi_todo_sistema()
    return 'Adeus'