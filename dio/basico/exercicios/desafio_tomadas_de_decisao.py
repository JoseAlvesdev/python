saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

def sacar(saldo_total=saldo_total, valor_saque=valor_saque):
  saldo_total -= valor_saque
  
  return saldo_total

  
if (valor_saque <= saldo_total):
  saldo_total = sacar()
  print(f"Saque realizado com sucesso. Novo saldo: {saldo_total}")
else:
  print("Saldo insuficiente. Saque nao realizado!")