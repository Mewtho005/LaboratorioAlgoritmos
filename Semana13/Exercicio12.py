def main():
    kg_colhidos = []
    preco_por_kg = []
    valor_por_arvore = []

    print("Digite os kg colhidos por árvore:")
    for i in range(5):
        kg_colhidos.append(float(input()))

    print("Digite o preço por kg:")
    for i in range(5):
        preco_por_kg.append(float(input()))

    for i in range(5):
        valor = kg_colhidos[i] * preco_por_kg[i]
        valor_por_arvore.append(valor)

    print("Valor obtido por árvore:")
    print(valor_por_arvore)

main()
