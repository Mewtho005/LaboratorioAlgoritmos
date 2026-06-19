#Ler vagas.
#Contar ocupadas.
#Contar livres.
#Mostrar relatório.

def vagas():
    return int(input("Ver vagas:"))

def ocupada():
    return int(input("Ocupadas:"))

def livres():
    return int(input("Livres:"))

def relatorio(v,o):
    livres = v - o
    return livres



def main():
    v = vagas()
    o = ocupada()

    l = relatorio(v,o)

    print("Vagas Livres", l)

main()
