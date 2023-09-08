frutas = ["maça", "banana", "limão", "uva"]

print(f"""-------------------------------------------
                    MÉTODO append()
""")


frutas.append("mamão")
print(frutas)

print("-------------------------------------------")

frutas.clear()
print(frutas)

print("-------------------------------------------")

frutas = ["maça", "limão", "banana", "limão", "uva", "uva"]

print(frutas.count("limão"))

print("-------------------------------------------")

frutas = ["maça", "banana", "limão", "uva"]

frutas_2 = (frutas.copy())
print(frutas_2)

print(id(frutas_2))