"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

Exemplos SyntaxError

a)
def funcao:
    print('Geek University')

 # SyntaxError: expected '('

b)
def = 1

#SyntaxError: cannot assign to None

c)
return

# SyntaxError: 'return' outside function

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a) 
print(geek)

b)
geek()

c)
a = 18

if a < 10:
    msg = 'E maior que 10'

print(msg)

# NameError: name 'geek' is not defined

3 - TypeError -> Ocorre quando uma funçao e aplicada a um tipo errado.

a)
print(len(2))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado ultilizando um índice inválido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[2][10])

c)
tupla = ('Geek')
print(tupla[2][10])

# IndexError: string index out of range

5 - ValueError -> ocorre quando uma função  bult-in (integrada) recebe um argumento como tipo correto mas valor inapropiado.

Exemplos ValueError

a)
print(int('Geek'))

# ValueError: invalid literal for int() with base 10: 'Geek'

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dic = {'geek': 'University'}
print(dic['python'])

# KeyError: 'python'

7 -AttributeError -> Ocorre quando uma variavel não tem um atributo ou função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 5)
tupla.sort()
print(tupla)

# AttributeError: 'tuple' object has no attribute 'sort'

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

a)
def nova():
print('Geek')

nova()

b)
for i in range(1, 11):
print(i + 1)

c)


# IndentationError: expected an indented block after function definition on line 110

OBS.: Execptions e Erros são sinônimos na progração.

OBS.: Importante ler e prestar atenção na saída de erro.
"""
# Exemplos KeyError
