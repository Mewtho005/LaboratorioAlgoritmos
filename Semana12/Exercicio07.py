def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custoFinal = custo + imposto
    
    return custoFinal

def main():
    custo = float(input("Digite o custo do item: "))
    taxa = float(input("Digite a taxa de imposto (%): "))
    
    valorFinal = somaImposto(taxa, custo)
    
    print("Valor com imposto: R$", valorFinal)

main()
