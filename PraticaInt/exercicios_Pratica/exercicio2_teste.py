# testando fazer um codigo para quantos elementos o usuario quer em uma lista

listona = []

num = input("Quantos elementos deseja na lista? ")
num1 = int(num)

def tamanho(num1):
    for i in range(num1):
        result = input(f"Digite o {i+1}º elemento da lista: ")
        listona.append(int(result))
    return listona
        
lst = tamanho(num1)
soma = sum(lst)

print(f"lista final {lst}")
print(f"Soma dos elementos da lista: {soma}")

print("\n\n\n")
