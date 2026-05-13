num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

for numero in range(num1, num2 + 1):
    if numero % 2 == 0:
        print(numero)
