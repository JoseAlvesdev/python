class Funcionario:
    empresa = 'Bar do Tio Juca'
    
    def __init__(self, cpf, nome, salario):
        self._cpf = cpf
        self._nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario or self._salario
    
    @salario.setter
    def salario(self, gorgeta):
        self._salario += gorgeta

    @salario.deleter
    def salario(self):
        self._salario = 0


funcionario = Funcionario('00011122233', 'Paula Fernandes Cantora de Bar', 1300)
funcionario.salario = 500
print(funcionario._salario)
del funcionario.salario
print(funcionario._salario)