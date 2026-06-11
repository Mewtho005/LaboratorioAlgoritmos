def maiorMenor(producoes):
    maior = max(producoes)
    menor = min(producoes)

    indiceMaior = producoes.index(maior)
    indiceMenor = producoes.index(menor)

    print("Maior produção:", maior, "kg")
    print("Posição do maior valor:", indiceMaior)

    print("Menor produção:", menor, "kg")
    print("Posição do menor valor:", indiceMenor)

def main():
    producoes = []

    for i in range(5):
        kg = int(input("Digite a produção da árvore", i, "(kg): "))
        producoes.append(kg)

    maiorMenor(producoes)

main()
