import unittest

from atividades import comer, dormir, eh_egracada


# classs [modulo_name''Test](unittest.TestCase):
class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormindo_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )
    
    def test_dormindo_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        #self.assertEqual(eh_egracada('Sérgio Malandro'), False)
        self.assertFalse(eh_egracada('Sérgio Malandro'))
        self.assertTrue(eh_egracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()