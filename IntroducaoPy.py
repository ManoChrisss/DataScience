num_notas = int(input("Quantas notas serao digitadas? "))

soma = 0
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i+1} do aluno: "))
    soma += nota

media = soma / num_notas
if media >= 9:
    print(f"Aprovado e destaque do bimestre com media {media}")
elif media >= 6 and media < 9:
    print(f"Aprovado com media {media:.1f}")
elif media <= 6 and media >= 4:
    print(f"Recuperação com media {media:.1f}")
elif media <= 4:
    print(f"Reprovado com media {media:.1f}")