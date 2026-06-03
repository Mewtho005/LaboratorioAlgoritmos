def calcularMedia():
    soma = 0
    
    for i in range(5):
        nota = float(input("Digite a nota: "))
        soma += nota
    
    media = soma / 5
    return media

def aprovado():
    print("Aluno Aprovado")

def recuperacao():
    print("Aluno em Recuperação")

def reprovado():
    print("Aluno Reprovado")

def main():
    media = calcularMedia()
    
    print("Média:", media)
    
    if media >= 7:
        aprovado()
    elif media >= 4 and media < 7:
        recuperacao()
    else:
        reprovado()

main()
