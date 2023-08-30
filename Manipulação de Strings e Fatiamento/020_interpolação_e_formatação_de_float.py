nome = "José"
idade = 22
profissao = "Programador"
linguagem = "Python"
numero = 10.5
saldo = 45.384

dados = {"nome": "José", "idade": 22, "saldo": 45.435} #dicionário

print("Nome: %s Idade: %d Número: %f" % (nome, idade, numero))
print("Nome: {} Idade: {} Número: {}" .format(nome, idade, numero))
print("Nome: {2} Idade: {1} Número: {0}" .format(numero, idade, nome)) #Variavel sendo passada numerada.
print("Nome: {2} Idade: {1} Número: {0} [{2} {2}]" .format(numero, idade, nome)) #Posso usar quantas vzs precisar INTERESSANTE.
print("Nome: {nome} Idade: {idade} Número: {numero}" .format(nome = nome, idade = idade, numero = numero)) #Variavel sendo passada nomeada.
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f" Nome: {nome} Idade: {idade} Saldo: {saldo:4.2f}") #formatação de um float
