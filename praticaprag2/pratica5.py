#Crie uma função que leia 5 números para um vetor e outra função que mostre todos os números.

def lernumero():
    vetor = []

    for i in range(5):
        numero = int(input("Digite um numero: "))
        vetor.append(numero)
    return vetor

def mostra(vetor):
    print(vetor)

def main():
    vetor = lernumero()

    mostrar = mostra (vetor)

main()
