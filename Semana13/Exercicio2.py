#Leia um array com 8 valores de produção de azeitonas em kg. Calcule a média e exiba quais produções ficaram acima da média.

def ler_producoes():
    producoes = []

    for i in range(8):
        valor = float(input(f"Digite a produção {i+1} em kg: "))
        producoes.append(valor)

    return producoes


def calcular_media(vetor):
    soma = 0

    for i in range(len(vetor)):
        soma += vetor[i]

    media = soma / len(vetor)

    return media


def mostrar_acima_media(vetor, media):

    print(f"Média da produção: {media:.2f} kg")
    print("Produções acima da média:")

    for i in range(len(vetor)):

        if vetor[i] > media:
            print(vetor[i], "kg")


def main():

    producoes = ler_producoes()

    media = calcular_media(producoes)

    mostrar_acima_media(producoes, media)


main()
