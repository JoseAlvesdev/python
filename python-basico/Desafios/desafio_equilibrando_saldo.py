saldo_atual = float(input('Digite o saldo atual: '))
reposta_usuario_continuar = 'none'

while (reposta_usuario_continuar != 'N' and 'n'):

    menu = f'''
============================
|          DIOBANK         |
============================
|                          |
| Saldo Atual              |
|                          |
|   R$ {saldo_atual:.1f}              
| ........................ |
|                          |
| Extrato                  |
|                          |
|   ...                    |
|                          |
|                          |
============================
|           MENU           |
============================
|   [1] Depositar          |
|   [2] Sacar              |
============================
'''
    print(menu)

    resposta_usuario = int(input('| Selecione uma opção: '))

    if (resposta_usuario == 1):

        valor_deposito = float(input('| Digite o valor: R$ '))

        saldo_atual += valor_deposito
        print(f'''
============================
|          DIOBANK         |
============================
|                          |
| Saldo Atual              |
|                          |
|   R$ {saldo_atual:.1f}              
| ........................ |
|                          |
| Extrato                  |
|                          |
|   Depósito...  +{valor_deposito:.1f}                  
|                          |
| ........................ |
|                          |
|    TRANSAÇÃO EFETUADA    |
|       com sucesso!!      |
============================
|           MENU           |
============================
|   [1] Depositar          |
|   [2] Sacar              |
============================
''')

    elif (resposta_usuario == 2):

        valor_retirada = float(input('| Digite o valor: R$ '))
       
        if (valor_retirada <= saldo_atual):

            saldo_atual -= valor_retirada

            print(f'''
============================
|          DIOBANK         |
============================
|                          |
| Saldo Atual              |
|                          |
|   R$ {saldo_atual:.1f}              
| ........................ |
|                          |
| Extrato                  |
|                          |                   
|   Saque...     -{valor_retirada:.1f}                       
|                          |
| ........................ |
|                          |
|    TRANSAÇÃO EFETUADA    |
|       com sucesso!       |
============================
|           MENU           |
============================
|   [1] Depositar          |
|   [2] Sacar              |
============================
''') 
            
        else:
            
            print(f'''
============================
|          DIOBANK         |
============================
|                          |
| Saldo Atual              |
|                          |
|   R$ {saldo_atual:.1f}              
| ........................ |
|                          |
| Extrato                  |
|                          |                   
|   ...                    |
| ........................ |  
|                          |
|  TRANSAÇÃO NÃO EFETUADA! |
|                          |
| O VALOR que está tentando|
| SACAR e maior que o      |
| saldo atual.             |
============================
|           MENU           |
============================
|   [1] Depositar          |
|   [2] Sacar              |
============================
''')
            
    else:

        print('| RESPOSTA INVÁLIDA \n| revise sua reposta e tente novamente!')
        
    reposta_usuario_continuar = input('| Deseja continuar? [S | N]: ')

    if (reposta_usuario_continuar == 'N' or reposta_usuario_continuar == 'n'):
        break

'''

'''