oliveiras = 0
maior = -1
menor = 100000
dias = 1
total = 0
dia_menor = 0
dia_maior = 0

while dias <= 7:
    oliveiras = int(input("Digite a quantidade de oliveiras colidas: "))
    total += oliveiras

    if oliveiras < menor:
        menor = oliveiras
        dia_menor = dias

    if oliveiras > maior:
        maior = oliveiras
        dia_maior = dias

    dias += 1

print("Total:", total)
print("Dia com menos:", dia_menor)
print("Dia com mais:", dia_maior)
