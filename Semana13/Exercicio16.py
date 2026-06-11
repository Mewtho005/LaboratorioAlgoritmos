import random

def gerarPragas():
    return random.sample(range(1, 101), 5)

def confrontar(colheita, pragas):
    protegidos = 0
    perdidos = 0

    print("Forças da equipe:", colheita)
    print("Forças das pragas:", pragas)
    print()

    for i in range(5):
        print("Lote", i)

        if colheita[i] > pragas[i]:
            print("Resultado: Protegido")
            protegidos += 1
        else:
            print("Resultado: Praga resistiu")
            perdidos += 1

    print()
    print("Placar final:", protegidos, "lotes protegidos x", perdidos, "lotes perdidos")

def main():
    colheita = []

    print("Digite as forças da equipe para os 5 lotes:")

    for i in range(5):
        forca = float(input("Lote " + str(i) + ": "))
        colheita.append(forca)

    pragas = gerarPragas()

    confrontar(colheita, pragas)

main()
