#Crie uma função que leia a produção de 5 lotes e outra que retorne a produção total.

def lerlotes():
    vetor = []

    for i in range(5):
        numero = int(input("Digite os lotes: "))
        vetor.append(numero)
    return vetor

def producaototal(vetor):
    soma = 0

    for valor in vetor:
        soma += valor
    return soma
    
def main():
    
    lotes = lerlotes()

    total = producaototal(lotes)

    print("Produção total: ", total)

main()
