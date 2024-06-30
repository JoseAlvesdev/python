"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

# dunder initi -> __init__()
def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

# Dunder > Double Underscore

dunder repr -> Representação do objeto
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
    
    # O método __str__ tem preferência ou seja onde há 
    # __repr__ e __str__, __str__ têm preferência.
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return len(self.titulo)
    
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'
    


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligencia Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)

