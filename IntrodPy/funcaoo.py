def imprime():
    print("Esta é uma funcao")
imprime()

print("\n")

#Def com parametro

def imprime(n): #coloco um valor qualquer para n (um parametro qualquer, ou seja, posso fazer qualquer coisa na funcao imprime)
    print(n) #coloquei para printar, ou seja, quando eu colocar qualquer str na def imprime ele vai printar
imprime("Impressão deste texto")

print("\n")

def soma(a,b):
    print(a+b)
soma(100,200)

print("\n")

#Def com retorno
def potencia(n):
    return n * n 
x = potencia(3)

print("\n")

#def com valor default

def intervalo (inicio = 1, fim = 10):
    for i in range(1, fim + 1):
        print(i)
intervalo(1, 10)
intervalo()

print("\n")

