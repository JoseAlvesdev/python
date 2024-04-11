import threading # 1
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10)) # 2

    th.start() # Adiciona a nossa thread na pool de threads prontas para
    # execução # 3

    print(
        'Podemos fazer outras coisas no programa enquanto a thread vai '
        'executando'
    )

    print('Geek Uniniversity ' * 2)

    th.join() # Avisa para ficar aguardando aqui até a thread terminar a
    # funcão # 4

    print('Pronto!')


def contar(str, num):
    for i in range(1, num + 1):
        print(i, str)
        time.sleep(1)


if __name__ == '__main__':
    main()
