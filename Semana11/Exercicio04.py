vetorA = []

while len(vetorA) < 10:
    numero = int(input(f"Digite o {len(vetorA)+1}º valor: "))

    if numero not in vetorA:
        vetorA.append(numero)
    else:
        print("Valor repetido! Digite outro número.")

vetorB = []

for i in range(9, -1, -1):
    vetorB.append(vetorA[i])

print("Vetor A: ")
print(vetorA)

print("Vetor B (ordem inversa): ")
print(vetorB)
