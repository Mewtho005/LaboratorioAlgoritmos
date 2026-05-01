contador = 0
i = 1

while i <= 10:
    idade = int(input("Digite a idade da pessoa: "))

    if idade >= 18:
        contador = contador + 1

    i = i + 1

print("Quantidade de pessoas com 18 anos ou mais:", contador)
