"""
Seek e Cursors

seek() é utilizada para movimentar o cursor pelo o arquivo

arquivo = open('texto.txt')

print(arquivo.read())

# Movimentando o cursor pelo o arquivo com a função seek() -> procurar().

# seek() -> A função seek() é utilizada para movimentação do cursor pelo
# o arquivo. Ela recebe um parâmetro que indica onde queremos colocar o
# cursor

arquivo.seek(0) 

print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha readline() -> lelinha()

ret = arquivo.readline()

print(type(ret))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão
entre o arquivo no disco do computador e o nosso programa. Essa conexão e
chamada de streaming. Ao finalizar os trabalhos com os arquivos devemos 
fechar essa conexão. Para isso utilizaremos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Tralhando o arquivo;
print(arquivo.read())

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado.

# 3 - Fechar o arquivo;
arquivo.close()
print(arquivo.closed) # True

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
"""
arquivo = open('texto.txt')

# Limitando a leitura somente aos primeiros 50 caracteres.
print(arquivo.read(50))


