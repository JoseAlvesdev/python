opcao = -1

while opcao != 0:
    opcao = int(input("[1] SACAR \n[2] EXTRATO \n[0] SAIR \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Saindo...")