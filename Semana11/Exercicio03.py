vetor = []

while len(vetor) < 10:
    numero = int(input(f"Digite o {len(vetor)+1}º valor: "))

    if numero not in vetor:
        vetor.append(numero)
    else:
        print("Valor repetido! Digite outro número.")

print("Valores pares e suas posições: ")

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print(f"Valor: {vetor[i]} | Posição: {i}")
