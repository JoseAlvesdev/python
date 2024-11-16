import multiprocessing

def calcular(data):
    return data ** 2


def main():
    # Pega a quantidade de processadores da minha máquina e multiplica por 2 que da um total de 32
    tamanho_pool = multiprocessing.cpu_count() * 2

    print(f'Tamanho da Pool: {tamanho_pool}')

    # Aqui estou definindo a quantidade de processos da minha Pool (piscina)
    pool = multiprocessing.Pool(processes=tamanho_pool)
    print(pool)

    # Criando nossas entradas
    entradas = list(range(7))

    # Criando as saidas
    saidas = pool.map(calcular, entradas)

    print(f'Saidas: {saidas}')

    # Aqui estou dizendo não tenho más nenhuma função pra mapear pode
    # iniciar os processos
    pool.close()

    # Cada processo que foi criado execute até o fim
    pool.join()


if __name__ == '__main__':
    main()