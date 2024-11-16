import multiprocessing

def ping(conn):  # conn = conexão
    conn.send('Geek')  # Envia o dado (send de enviar)


def pong(conn):
    msg = conn.recv() # Recebe o dado do outro processo (recv de receber)
    print(f'{msg} University')


def main():
    conn1, conn2  = multiprocessing.Pipe(True)  # Pipe e o que conecta os processo como se fosse um cano
    # Pipe(duplex=True) -> Estou dizendo que ambos os meu processos vão enviar e receber dados
    # Pipe(duplex=False) -> Estou dizendo somente um dos processos pode enviar e outro somente receber dados.

    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()