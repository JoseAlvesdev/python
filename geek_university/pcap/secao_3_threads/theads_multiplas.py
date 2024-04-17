import threading # 1
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12))
    ] # 2

    [thread.start() for thread in threads]
    # Adiciona a nossa thread na pool de threads prontas para
    # execução # 3

    print(
        'Podemos fazer outras coisas no programa enquanto a thread vai '
        'executando'
    )

    print('Geek Uniniversity ' * 2)

    [thread.join() for thread in threads] 
    # Avisa para ficar aguardando aqui até a thread terminar a
    # funcão # 4

    # Não execute o programa enquanto essas threads não finalizar

    print('Pronto!')


def contar(str, num):
    for i in range(1, num + 1):
        print(i, str)
        time.sleep(1)


if __name__ == '__main__':
    main()