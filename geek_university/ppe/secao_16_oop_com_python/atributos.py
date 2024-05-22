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
"""


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