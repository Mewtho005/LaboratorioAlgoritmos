#Gerar força do herói.
#Gerar força do monstro.
#Realizar combate.
#Mostrar vencedor final.

def hforca():
    return int(input())
    
def mforca():
    return int(input())

def combate(h,m):
    if h > m:
        return ("Heroi Venceu")
    elif h < m:
        return ("Monstro Venceu")
    else:
        return ("Empate")


def main():
    h = hforca()
    m = mforca()
    resultado = combate(h,m)
    print(resultado)


main()
