# Funçao que recebe uma string e retorna na vertical

vert = input("Digite uma palavra: ")

def vertical(vert):
    for i in range (0, len(vert)):
        print(vert[i])

print(f"a palavra {vert} tem {len(vert)} letras e na vertical fica:")

vertical(vert)
