vetor = []
maiores_que_30 = 0
soma_maiores = 0
soma_total = 0

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print("Valores do vetor: ")
for num in vetor:
    print(num)

    soma_total += num

    if num > 30:
        maiores_que_30 += 1
        soma_maiores += num

print(f"\nQuantidade de números maiores que 30: {maiores_que_30}")
print(f"Soma dos números maiores que 30: {soma_maiores}")
print(f"Soma de todos os números: {soma_total}")
