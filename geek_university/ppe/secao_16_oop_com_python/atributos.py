"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python dividimos os atributos em 3 grupos:
  - Atributos de instância;
  - Atributos de classe;
  - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método contrutor: É um método especial utilizado para a construção
do objeto.

# Em Java classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada() {
    private int voltagem;
    private String cor;
    private Boolean ligada =  false;

    public Lampada(int voltagem, String cor) {
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python por convenção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo dever ser tratado como
privado, ou seja, que dever ser acessado/utilizado somente dentro da própria 
clase onde está declarado, utliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
# não vai impedir que façamos acesso aos atributos sinalizados como privados
# fora da classe.

# Exemplo

user = Acesso('example@gmail.com', 'user@123')

#print(user.__senha) # AttributeError

#print(dir(user._Acesso__senha)) # Temos acesso. Mas não deveriamos fazer este acesso. (Name Mangling)

print(user.exibir_senha())
print(user.email)

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as
# instâncias terão estes atributos.

user1 = Acesso('example@gmail.com', '3k48i2')
user2 = Acesso('example@gmail.com', '0j823k')

print(user1.email, user2.email, sep='\n')

# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente 
# na classe, ou seja, fora do contrutor. Geralmente já inicializamos um valor,
# e este valor é compartilhado entre todas as instâncias da classe. Ou seja,
# ao invés de cada instância da classe ter seus própios valores como é o caso
# dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

p1 = Produto('PlayStation 4', 'Video Game', 2300) # Acesso possível, mas incorreto de um atributo de classe
p2 = Produto('Xbox S', 'Video Game', 4500) # Acesso possível, mas incorreto de um atributo de classe

print(p1.valor, p2.valor, sep='\n')

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso
# a um atributo de classe.

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id, p2.id, sep='\n')

# OBS: Em linguagems como Java, os atributos conhecidos como atributos de classe
# aqui em Python são chamados de atributos státicos;
"""


# Classes com Atributo de Instância Público


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero =  numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def exibir_senha(self):
        return self.__senha
    
    def exibir_email(self):
        return self.email




# Refatorar a classe produto


class Produto:

    # Atributo de classe
    imposto = 1.05 # Atributo igual para todas as instâncias (objetos) da classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributo Dinâmicos -> Um atributo de instância que pode ser criado em 
# tempo de execução

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Alimento', 5.99)

# Criando um atributo dinânmico em tempo de execução

p2.peso = '5kg' # Note que na classe Produto não existe peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
#print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos dinâmicos e não dinâmicos 

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor

print(p1.__dict__)
print(p2.__dict__)