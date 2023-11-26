# pessoa = {'nome': 'José', 'idade': 22}

# pessoa = dict({'nome': 'José', 'idade': 22})

# pessoa['telefone'] = '62 99160-5900'

# print(pessoa)

pessoa = {
    'josehenriques10@outlook.com': {'nome': 'José', 'idade': 22, 'telefone': '62 99160-5900'}
}


#print(pessoa['josehenriques10@outlook.com']['nome'])

'''for chave in pessoa:
    print(chave, pessoa[chave])
'''
for chave, valor in pessoa.items():
    print(chave, valor)