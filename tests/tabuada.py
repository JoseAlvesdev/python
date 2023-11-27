class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def mostrar_tabuada(self):
        i = 1
        tabuada = []
        tabuada.append(f'\nTABUADA DO {self.numero}\n')

        while True:
            resultado = self.numero * i

            tabuada.append(f'{self.numero} x {i} = {resultado}')

            i += 1

            if i > 10:
                break

        for item in tabuada:
            print(item)

        return


def main():
    i = 1

    while True:
        tabuada = Tabuada(i)
        tabuada.mostrar_tabuada()

        i += 1

        if i > 3: break


main()