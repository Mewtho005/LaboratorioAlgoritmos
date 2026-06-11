def inverterProducao(producao):
    for i in range(len(producao) - 1, -1, -1):
        print(producao[i])

def main():
    producao = []

    for i in range(5):
        kg = float(input("Digite a produção em kg: "))
        producao.append(kg)

    print("Produções em ordem inversa:")
    inverterProducao(producao)

main()
