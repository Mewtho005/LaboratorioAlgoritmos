pares = 0
impares = 0
zeros = 0

for i in range(11):
    numero = int(input("Digite um numero:"))

    if numero == 0:
        zeros += 1
    
    if numero % 2 == 0:
        pares += 1

    else:
        impares += 1

print("Pares", pares)
print("Impares", impares)
print("Zeros", zeros)
