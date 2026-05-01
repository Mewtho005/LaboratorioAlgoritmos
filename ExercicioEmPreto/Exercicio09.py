idade = -1
while idade < 0 or idade > 150:
    idade = int(input("Digite a idade: "))

salario = 0
while salario <= 0:
    salario = float(input("Digite o salário: "))

sexo = ""
while sexo != "f" and sexo != "m":
    sexo = input("Digite o sexo (f ou m): ")

estado_civil = ""
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Digite o estado civil (s, c, v, d): ")

print("Dados cadastrados com sucesso!")
