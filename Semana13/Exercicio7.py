def calcularAzeite(lotes, rendimento):
    for i in range(len(lotes)):
        litros = lotes[i] * rendimento
        print("Lote", i, ":", litros, "litros de azeite")

def main():
    lotes = []

    for i in range(6):
        kg = float(input("Digite os kg de azeitona do lote: "))
        lotes.append(kg)

    rendimento = 0.18

    calcularAzeite(lotes, rendimento)

main()
