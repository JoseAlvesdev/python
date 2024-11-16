import multiprocessing

# Pegando o nome do processo e imprimindo
print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')

def faz_algo(value):
    print(f'Fazendo algo com o {value}')


def main():
    # Criando um Processo e alterando seu nome
    pc = multiprocessing.Process(target=faz_algo, kwargs={"value": "Pássaro"}, name='Processo Geek')

    # Pegando o nome do processo e imprimindo
    print(f'Iniciando o processo com nome: {pc.name}')

    # Inicando o processo
    pc.start()

    # Aguardando o processo terminar
    pc.join()


if __name__ == '__main__':
    main()