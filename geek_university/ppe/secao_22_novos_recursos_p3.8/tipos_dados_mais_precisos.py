"""
int, str, float, List, Set, Dict, etc...
"""


# def dobro(valor: int) -> int:
#     return valor * 2


# print(dobro(8))
# print(dobro('Geek'))

"""
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols
"""

# ==================================================
# Literal type

# from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass


# def calcula_v1(operacao: str, num1: int, num2: int) -> None:
#     match operacao:
#         case '+':
#             print(f'{num1} + {num2} = {num1 + num2}')
#         case '-':
#             print(f'{num1} - {num2} = {num1 - num2}')
#         case _:
#             raise ValueError(f'Operação inválida {operacao!r}') # !r coloca qualquer valor entre aspas


# def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
#     match operacao:
#         case '+':
#             print(f'{num1} + {num2} = {num1 + num2}')
#         case '-':
#             print(f'{num1} - {num2} = {num1 - num2}')
#         case _:
#             raise ValueError(f'Operação inválida {operacao!r}')


# calcula_v2('+', 6, 4)
# calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)

# ==================================================
# Union
# from typing import Union


# def soma(num1: int, num2: int) -> Union[str, int]:
#     resultado: int = num1 + num2
    
#     if resultado > 50:
#         return f'O valor {resultado} é muito grande.'
#     else:
#         return resultado
    
# ==================================================
# Final
# from typing import Final

# # Cria uma constante
# NOME: Final = 'Geek'

# print(NOME)

# # NOME = 'University'

# # print(NOME)

# from typing import final

# # Decorando um classe com o final, significa que nenhuma outra classe pode extende-la
# @final
# class Pessoa:
#     pass


# class Estudante():
#     pass

#     # Decorando um metodo com @final, significa que as classes filhas não podem sobrescrever esse método (AINDA NÃO FUNCIONA)
#     @final
#     def estudar(self):
#         print('Estou estudando...')


# class Estagiario(Estudante):
#     print('Estudando e estagiando')

# ==================================================
# Typed Dictionaries

# from typing import TypedDict

# class CursoPython(TypedDict):
#     versao: str
#     atualizacao: int


# geek = CursoPython(versao='3.8.5', atualizacao=2020)

# print(geek)

# outro = CursoPython(algo='vai', coisa=True)

# print(outro)


from typing import TypedDict

class Routes(TypedDict):
    rota1: str
    rota2: str


rotas: Routes = {'rota1': 'rota1', 'rota2': 1}