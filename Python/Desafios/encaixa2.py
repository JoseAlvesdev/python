n = int(input())

while(n > 0):
    A, B = input(" ").split()
    n = n - 1

    if A[-len(B):]. find (B) != -1:
        print("encaixa")
    else:
        print("nao encaixa")
