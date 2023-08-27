texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # quebra de linha
    
# Exemplo utilizando a função built-in range.
for numero in range(0, 51, 5):
    print(numero, end=" ")