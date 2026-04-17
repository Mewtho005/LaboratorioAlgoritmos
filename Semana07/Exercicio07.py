soma = 0
contador = 0

while contador < 15:
    idade = int(input("Digite a idade: "))
    soma += idade
    contador += 1

media = soma / 15

print("Média:", media)

if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
