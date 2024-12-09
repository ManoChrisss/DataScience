#Peso de carga em numeros

carga = (input("Qual o peso da carga? "))

carga2 = float(carga)

if carga2 <= 10:
    print(f"A carga de {carga2}kg é considerada uma carga leve. O valor será de R$ 50,00.")
elif carga2 > 11 and carga2 <= 20:
    print(f"A carga de {carga2}kg é considerada uma carga moderada. O valor será de R$ 80,00.")
else:
    print(f"Infelizmente, por sua carga possuir {carga2}kg o transporte não é aceito.")

