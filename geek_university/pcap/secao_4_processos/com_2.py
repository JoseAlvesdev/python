"""
Ah duas formas de comunicação entre processos
    - Pipe -> Não tem possibilidade de realizar locks e unlocks
    - Queue -> Possibilita a realização de locks e unlocks
"""

import multiprocessing

def ping(queue):
    queue.put('Geek') # Envia o dado


def pong(queue):
    msg = queue.get() # Recebe o dado do outro processo
    print(f'{msg} University')


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
