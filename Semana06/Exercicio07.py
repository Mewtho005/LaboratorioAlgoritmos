a = 0
b = 0
c = 0
i = 1

while i <= 10:
    bebida = input("Digite a bebida favorita (A, B ou C): ")

    if bebida == "A":
        a = a + 1

    elif bebida == "B":
        b = b + 1

    elif bebida == "C":
        c = c + 1

    i = i + 1

porc_a = (a / 10) * 100
porc_b = (b / 10) * 100
porc_c = (c / 10) * 100

print("Total de votos Café Expresso:", a)
print("Total de votos Cappuccino:", b)
print("Total de votos Chá:", c)

print("Porcentagem Café Expresso:", porc_a, "%")
print("Porcentagem Cappuccino:", porc_b, "%")
print("Porcentagem Chá:", porc_c, "%")
