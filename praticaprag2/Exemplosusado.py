#21/06
def ler_numeros():
    vetor = []

    for i in range(5):
        numero = int(input("Digite um número: "))
        vetor.append(numero)

    return vetor

def somar(vetor):
    soma = 0

    for numero in vetor:
        soma += numero

    return soma

def mostrar(vetor, soma):
    print("Vetor:", vetor)
    print("Soma:", soma)

def main():
    numeros = ler_numeros()

    resultado = somar(numeros)

    mostrar(numeros, resultado)

main()
