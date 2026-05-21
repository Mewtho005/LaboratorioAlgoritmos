vetor = []

while len(vetor) < 10:
    numero = int(input(f"Digite o {len(vetor)+1}º valor: "))

    if numero not in vetor:
        vetor.append(numero)
    else:
        print("Valor repetido! Digite outro número.")

maiores_100 = []

for num in vetor:
    if num > 100:
        maiores_100.append(num)

print("Valores maiores que 100: ")
for num in maiores_100:
    print(num)

print(f"Quantidade de valores maiores que 100: {len(maiores_100)}")
