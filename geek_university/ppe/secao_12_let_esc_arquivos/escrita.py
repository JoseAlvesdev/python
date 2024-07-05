"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura não podemos realizar a escrita 
nele. Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, 
não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema
operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a 
função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um
TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir 
será criado, caso ele já exista, o anterior será apagado e um novo será 
criado. Dessa forma, todo o conteúdo no arquivo anterior e perdido.

# Exemplo de escrita - modo 'w' - write (escrita)


# Forma Pythônica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a útima linha.')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('geek ' * 1000)

# Forma tradicional de escrita em arquivo (Não Pythônica)

arquivo = open('mais.txt', 'w')

arquivo.write('Novos dados.\n')
arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
arquivo.write('Esta é a útima linha.')

arquivo.close()

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(f'{fruta} ')
        else:
            break
"""
