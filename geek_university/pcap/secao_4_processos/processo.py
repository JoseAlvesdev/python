import multiprocessing
import multiprocessing.process

print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')

def faz_algo(value):
    print(f'Fazendo algo com o {value}')


def main():
    pc = multiprocessing.Process(target=faz_algo, kwargs={"value": "Pássaro"}, name='Processo Geek')

    print(f'Iniciando o processo com nome: {pc.name}')

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()