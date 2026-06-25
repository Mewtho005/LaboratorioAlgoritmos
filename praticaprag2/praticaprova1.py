def menu():
    print("1 - Cadastrar personagem")
    print("2 - Remover personagem")
    print("3 - Mostrar personagens")
    print("4 - Buscar personagem")
    print("5 - Sair")

    return int(input("Escolha: "))

def cadastrar(nomes, niveis):
    nome = input("Nome: ")
    nivel = int(input("Nivel: "))

    nomes.append(nome)
    niveis.append(nivel)

def mostrar(nomes, niveis):
    for i in range(len(nomes)):
        print(nomes[i], "-", niveis[i])

def remover(nomes,niveis):
    nome = input("Nome para remover: ")

    for i in range(len(nomes)):
        if nomes[i] == nome:
            nomes.pop(i)
            niveis.pop(i)
            print("Personagem removido!")
            return
    print("Personagem nao encontrado! ")

def buscar(nomes, niveis):
    nome = input("Nome para buscar: ")
    
    for i in range(len(nomes)):
        if nomes[i] == nome:
            print("Personagem encontrado!")
            print("Nome: ", nomes[i])
            print("Nível: ", niveis[i])
            return
    print("Personagem não encontrado! ")
    



def main():
    nomes = []
    niveis = []

    while True:
        op = menu()

        if op == 1:
            cadastrar(nomes,niveis)
        elif op == 2:
            remover(nomes, niveis)
        elif op == 3:
            mostrar(nomes, niveis)
        elif op == 4:
            buscar(nomes, niveis)
        elif op == 5:
            break
main()
