from importlib import metadata

# print(metadata.version('pip'))

# metadados_pip = metadata.metadata('pip')

# print(list(metadados_pip))

# print(metadados_pip['Project-URL']) # Retorna um tipo de dado específico 
# por isso estou acessando como um dicionario.

# print(len(metadata.files('pip')))

print(metadata.requires('django'))