"""
POO - O método super()

O método super() se refere a super classe.


"""


class Animal:

    def __init__(self, nome, specie):
        self.__nome = nome
        self.__specie = specie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, specie, raca):
        # Animal.__init__(self, nome, specie)
        super().__init__(nome, specie) # recomendado
        super().faz_som('Beeee')
        self.__raca = raca


felix = Gato('Felix', 'felino', 'Angorá')

felix.faz_som('Minheeuuu')