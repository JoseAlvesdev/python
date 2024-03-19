"""
Dunder Name e Dunder Main

Dunder -> Doble Under

Dunder Name -> __name__

Dunder Main -> __main__

Em python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programção.

# Na linguagem C, temos um programa da seguinte forma:

int main() {
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public statc void main(String[] args) {

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo e o
módulo principal.

from modulos import soma_impares

print(soma_impares(list(range(1, 11))))
"""
import primeiro
import segundo