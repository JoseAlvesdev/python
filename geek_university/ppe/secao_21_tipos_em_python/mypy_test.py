# $ mypy mypy_test.py

# def cabecalho(texto: str, alinhamento: bool = True) -> str:
#     if alinhamento:
#         return f'{texto.title()}\n{'-' * len(texto)}'
#     else:
#         return f' {texto.title()} '.center(50, '#')
    

# print(cabecalho('geek university'))

# print(cabecalho('geek university', False))

# print(cabecalho('geek university', alinhamento=True))

# OBS.: mypy só funciona com o type hinting

def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f'{texto.title()}\n{'-' * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')
    

print(cabecalho('geek university'))

print(cabecalho('geek university', False))

print(cabecalho('geek university', alinhamento='geek'))