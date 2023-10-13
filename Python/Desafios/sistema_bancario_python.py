menu = f'''

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair 

'''

saldo = 0
deposito = 0
saque = 0
extrato = []
numeros_saques = 0
LIMITE_DESAQUES = 3
LIMITE_DOSAQUE = 500

def atualiza_saldoD(saldo=saldo, deposito=deposito):

    deposito = int(input('Digite o valor do depósito: '))
    saldo += deposito
    
    return saldo, deposito

def atualiza_saldoS(saldo=saldo, saque=saque, numeros_saques=numeros_saques):

    saque = int(input('Digite o valor do saque: '))
    numeros_saques += 1

    print(saldo)

    if saque > saldo:
        print('Você não pode sacar um valor maior que o saldo atual.')

    elif numeros_saques > LIMITE_DESAQUES:
        print('Você ja excedeu o limite de saques diários.')
    
    elif saque > LIMITE_DOSAQUE :
        print(f'O limite de saque para sua conta é de: {LIMITE_DOSAQUE}.')

    elif saque <= LIMITE_DOSAQUE and saque <= saldo:
        saldo -= saque
    
    return saldo, saque

while True:

    opcao = input(menu)

    if opcao == 'D':
        saldo, deposito = atualiza_saldoD()
        extrato.append(f'+{deposito}')

    elif opcao == 'S':
        saldo, saque = atualiza_saldoS()
        extrato.append(f'-{saque}')

    elif opcao == 'E':
        for transacao in extrato:
            print()
            print(f'{transacao}')

    elif opcao == 'Q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
    