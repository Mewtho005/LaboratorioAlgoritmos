dia = 0

while dia < 1 or dia > 365:
    dia = int(input("Digite o dia juliano (1 a 365): "))

if dia <= 59:
    print("Primeiro bimestre de 2022")

elif dia <= 120:
    print("Segundo bimestre de 2022")

elif dia <= 181:
    print("Terceiro bimestre de 2022")

elif dia <= 243:
    print("Quarto bimestre de 2022")

elif dia <= 304:
    print("Quinto bimestre de 2022")

else:
    print("Sexto bimestre de 2022")
