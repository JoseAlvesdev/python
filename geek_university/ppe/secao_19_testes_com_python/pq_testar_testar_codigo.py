"""
Por que testar nosso código?

Testes Automatizados!

        Aplicação Web
---------------------------------
|                               |
|   frontend e backend          |
---------------------------------
|   Testes automatizados        |
---------------------------------

Porque testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recursos da sua aplicação nao quebrem
      (alterem) recurso antigos;
    - Teste garantem que bugs (problemas) que foram corrigidos anteriormente
      continuem corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam
      novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por testes)

Com tdd é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer seu teste
      passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente
    - E uma vez que o teste passe, o recurso e considerado completo:

Estes estágios de desenvolvimento do TDD são quase como um mantra que o
desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)