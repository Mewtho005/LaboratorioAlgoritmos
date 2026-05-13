jornal_a = 0
jornal_b = 0
jornal_c = 0

for i in range(20):
    jornal = input("Qual jornal você lê mais? (A, B ou C): ").upper()

    if jornal == "A":
        jornal_a += 1
    elif jornal == "B":
        jornal_b += 1
    elif jornal == "C":
        jornal_c += 1

porcentagem_a = (jornal_a / 20) * 100
porcentagem_b = (jornal_b / 20) * 100
porcentagem_c = (jornal_c / 20) * 100

print("Porcentagem do jornal A:", porcentagem_a, "%")
print("Porcentagem do jornal B:", porcentagem_b, "%")
print("Porcentagem do jornal C:", porcentagem_c, "%")
