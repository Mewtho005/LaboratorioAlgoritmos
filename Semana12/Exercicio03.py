#Utilize duas funções para realizar os cálculos

def numero():
    n1 = float(input("Digite um numero: "))
    return n1

def calculardobro(numero1):
    dobro = numero1 * 2
    return dobro

def calculartriplo(numero2):
    triplo = numero2 * 3
    return triplo

def main():
    n = numero()
    
    dobro = calculardobro(n)
    triplo = calculartriplo(n)
    
    print("Dobro:", dobro)
    print("Triplo:", triplo)

main()
