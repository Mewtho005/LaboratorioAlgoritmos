def calcularCompra(quantidade):
    if quantidade <= 12:
        total = quantidade * 0.40
    else:
        total = quantidade * 0.25
    
    return total

def main():
    laranjas = int(input("Digite a quantidade de laranjas compradas: "))
    
    valorTotal = calcularCompra(laranjas)
    
    print("Valor total: R$", valorTotal)

main()
