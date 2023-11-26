saldo =500

saque = float(input("Digite o valor do saque: "))
status_da_operacao = "Sucesso" if saldo >= saque else "Falha"

print(f"{status_da_operacao} ao realizar o saque!")