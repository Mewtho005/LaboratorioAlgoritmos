#ler_notas()
#calcular_media()
#mostrar_resultado()

def lernota1():
    return float(input("Nota 1:"))
def lernota2():
    return float(input("Nota 2:"))
def calcular(l1,l2):
    media = (l1 + l2) / 2
    return media
def resultado(media):
    if media >= 70:
        return("Aprovado")
    elif media < 70:
        return("Exame")
    else:
        return("Reprovado")

def main():
    l1 = lernota1()
    l2 = lernota2()

    media = calcular(l1,l2)
    status = resultado(media)

    print(media)
    print(status)
main()
