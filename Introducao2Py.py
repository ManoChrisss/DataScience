num_func = int(input("Quantos funcionarios terão seu salário registrado?: "))

#Listas
funcionarios = []
for i in range(num_func):
    funcionario = input(f"Digite o nome do funcionario {i+1}: ")
    funcionarios.append(funcionario)

salarios = []
for i in range(num_func):
    salario = float(input(f"Digite o salario do {funcionarios[i]} : "))
    salarios.append(salario)

i = 0
while i < num_func and funcionario:
    print(f"Salário do {funcionarios[i]} é: R${salarios[i]:.2f}")
    i += 1