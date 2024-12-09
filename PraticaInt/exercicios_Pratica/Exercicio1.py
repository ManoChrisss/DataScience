# programa com funçao amplitude e recebe lista e printar amplitude

def amplitude(lista):
    amplitudes = max(lista) - min(lista)
    return amplitudes

def tamanho(lista):
    lenght = len(lista)
    return lenght

lst = [1,2,3,4,5]
resultado = amplitude(lst)
qnt = tamanho(lst)

print(f"Amplitude: {resultado}")
print(f"tamanho da lista: {qnt}")


print("\n\n\n")