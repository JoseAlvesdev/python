N = int(input())

while(N > 0):
    A_ = input()
    B_ = input()
    A = []
    B = []

    for caracter in A_:
        A.extend(caracter)
    for caracter in B_:
        B.extend(caracter)

    l, l_ = len(A), len(B)

    if l_ > l:
        l_ *= -1
        l *= -1
        for i in range(l_, l):
            A.extend('*')

    Count = len(B) * -1
    verificador = []
    c = 0

    for i in range(Count, 0):
        if B[i] == A[i]:
            verificador.append(1)
        else:
            verificador.append(-1)

    for i in range(Count, 0):
        if verificador[i] == 1:
            c += 1
        else:
            c += 0

    l = len(verificador)

    if c == l:
        print('encaixa')
    else:
        print('nao encaixa')

