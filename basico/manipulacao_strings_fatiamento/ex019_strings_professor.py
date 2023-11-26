nome = "jose"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá Mundo!    "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "    Python"

print("    "+menu+"    ")
print(menu.center(20, "#"))
menu.lstrip()
print("-".join(menu.upper()))