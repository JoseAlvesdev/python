import math

# math.prod - retorna o produto de um container numérico
# container númerico -> contém 2 ou mais números.
# nuns_v1 = list(range(2, 9, 2))
# nuns_v2 = tuple(range(2, 9, 2))
# nuns_v3 = set(range(2, 9, 2))

# =============================
# PRODUTO
# print(math.prod(nuns_v1))
# print(math.prod(nuns_v2))
# print(math.prod(nuns_v3))

# 2 * 4 * 6 * 8 -> 384

# =============================
# RAIZ QUADRADA
# math.isqrt

# isqrt -> Raiz quadrada inteira
# sqrt -> Raiz quadrada

# print(math.isqrt(9))
# print(math.sqrt(9))
# print(math.isqrt(17))
# print(math.sqrt(17))

# =============================
# DISTÂNCIA EUCLIDIANA
# math.dist -> distância euclidiana entre dois pontos, 3D ou 2D.

# PONTOS 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# PONTOS 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

# print(math.dist(p3d1, p3d2))
# print(math.dist(p2d1, p2d2))

# =============================
# HIPOTENUSA
# math.hypot -> retorna a hipotenusa, ou norma euclidiana

# print(math.hypot(*p3d1))
# print(math.hypot(*p2d1))

# Estatística
import statistics

# =============================
# FLOAT MEDIA
# statistic.fmean -> calcula a média de números reais

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

# print(statistics.fmean(valores_reais))
# print(statistics.fmean(valores_inteiros))

# =============================
# MÉDIA GEOMÉTRICA
# statistics.geometric_mean -> calcula a média geométrica de números reais.

# print(statistics.geometric_mean(valores_reais))
# print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode -> retorna o valor mais frequente em uma sequencia

seq1 ='Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))