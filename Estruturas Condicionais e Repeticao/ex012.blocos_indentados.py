saldo = 500

def sacar(valor: float):
    if (saldo >= valor):
        print("Valor sacado!")
        print("Retire seu dinheiro do caixa.")
    else:
        print("Saldo Insuficiente! :/")
        print("Tente novamente com outro VALOR!")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")     



sacar(1000)