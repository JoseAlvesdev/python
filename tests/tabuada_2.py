def mostrar_tabuada(stop:int, start:int=1) -> str:
    tabuada = ''

    for i in range(start, stop):
        tabuada += f'Tabuada do {i}\n'

        for j in range(1, 11):
            resultado = i * j
            tabuada += f'{i} x {j} = {resultado}\n'
            tabuada += '\n' if j == 10 else ''

    return tabuada


def main():
    print(mostrar_tabuada(11))


main()
