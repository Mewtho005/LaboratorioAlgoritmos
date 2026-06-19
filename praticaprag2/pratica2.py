#Gerar pragas.
#Ler colheita.
#Comparar resultados.
#Mostrar vencedor.

def praga():
    return int(input("Qnt Pragas"))

def colheita():
    return int(input("Qnt de colheita"))

def comparar(p,c):
    if p > c:
        return("Pragas venceram")
    elif c > p:
        return("Colheitas venceram")
    else:
        return("empate")

def main():
    p = praga()
    c = colheita()

    resultado = comparar(p,c)

    print(resultado)

main()
