numero = -1

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

    
for numero in range(100):

    if numero == 10:
        break#continue

    print(numero, end=" ")
