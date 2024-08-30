import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


#print(circunferencia(8))

#print(circunferencia('geek'))

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f'{texto.title()}\n{'-' * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')
    

# cabecalho(texto=43, alinhamento='geek')

def cabecalho2(
    texto,  # type: str
    alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


cabecalho2(texto=43, alinhamento='geek')

#nome = 'Geek University'  # type: str