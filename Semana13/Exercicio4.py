def calcularSomaEMedia(colheitas):
    soma = sum(colheitas)
    media = soma / len(colheitas)
    return soma, media

def main():
    colheitas = []

    for i in range(5):
        kg = int(input("Digite a quantidade de azeitonas colhidas (kg): "))
        colheitas.append(kg)

    soma, media = calcularSomaEMedia(colheitas)

    print("Soma total:", soma, "kg")
    print("Média por colheita:", media, "kg")

main()
