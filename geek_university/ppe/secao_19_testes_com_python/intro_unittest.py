"""
Introdução ao módulo Unittest

Unittest -> Teste Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é espeficico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase()
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Case de teste para sua unidade

# Conhecendo as assertions

documentação: https://docs.python.org/3/library/unittest.html

Métodos                     Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIsNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIn(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsInstance(a, b)      a é instância de b
assertNotIsInstance(a, b)   a não é instância de b

Por convernção, todos os testes em um test case, devem ter seu nome
iniciado com test_

Para executar os testes com unittest

$ python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrecentar (e é recomendado) docstrings nos nossos testes.
"""

# Prática - Utilizando a abordagem TDD