def leasnota():
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    return n1, n2

def calculamedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def situacao(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

def main():
    nota1, nota2 = leasnota()
    media = calculamedia(nota1, nota2)
    situacao(media)

main()
