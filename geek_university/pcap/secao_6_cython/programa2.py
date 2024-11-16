import datetime
import computa


def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=50_000_000)
    
    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


if __name__ == '__main__':
    main()


"""
Terminou em 10.74 segundos.
Terminou em 12.42 segundos. :[ # Sem usar os recursos do Cython
Terminou em 0.0 segundos. :] :]
Terminou em 0.0 segundos. Como Gil do Python completamente removido
"""