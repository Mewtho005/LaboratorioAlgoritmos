#Soma de fazendas. Crie dois arrays do mesmo tamanho com produções inteiras (kg) de Fazenda A e Fazenda B. 
#Gere um terceiro array com a soma elemento a elemento (produção total por posição/lote).

def ler_fazenda(nome, tamanho):

    vetor = []

    print(f"Produção da {nome}")

    for eu in range(tamanho):

        valor = int(input(f"Digite a produção do lote {eu+1}: "))
        vetor.append(valor)

    return vetor


def somar_fazendas(v1, v2):

    soma = []

    for esse in range(len(v1)):
        soma.append(v1[esse] + v2[esse])

    return soma


def mostrar_soma(vetor):

    print("Produção total por lote:")

    for porta in range(len(vetor)):
        print(f"Lote {porta+1}: {vetor[porta]} kg")


def main():

    tamanho = 5

    fazendaA = ler_fazenda("Fazenda A", tamanho)
    fazendaB = ler_fazenda("Fazenda B", tamanho)

    soma = somar_fazendas(fazendaA, fazendaB)

    mostrar_soma(soma)


main()  
