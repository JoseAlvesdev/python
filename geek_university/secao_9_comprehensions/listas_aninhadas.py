"""
Listas Aninhadas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

[[print(valor) for valor in matriz] for valor in matriz]

# Gerando tabuleiro(matriz) 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for linha in range(1, 4)]

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
"""


