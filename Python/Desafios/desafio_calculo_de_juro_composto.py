valor_inicial = float(input('a'))
taxa_juros = float(input('b'))
periodo = int(input('c'))

#M = C (1+i)t

def calcula_o_juro_composto(valor_final, taxa_juros, periodo):
  
  valor_final = valor_inicial * (1 + taxa_juros) ** periodo
  
  return valor_final


valor_final = calcula_o_juro_composto(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {valor_final:.2f}")