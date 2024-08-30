import time
from threading import Thread

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


thread1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
thread2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
fim = time.time()

print(f'Tempo em segundos - {fim - inicio}')

# Tempo em segundos - 1.4863357543945312