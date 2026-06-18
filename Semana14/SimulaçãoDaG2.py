from datetime import datetime, timedelta
import matplotlib.pyplot as plt

aeronaves = []
datas_entrada = []

espera = ""
espera_data = None

tempo_atual = datetime.now()

total_estacionamentos = 0
total_retiradas = 0
caixa = 0


def solicitar_vaga():
    global total_estacionamentos
    global espera
    global espera_data

    codigo = input("Digite o código da aeronave: ")

    if codigo in aeronaves or codigo == espera:
        print("Código já cadastrado.")
        return

    if len(aeronaves) < 5:
        aeronaves.append(codigo)
        datas_entrada.append(tempo_atual)

        total_estacionamentos += 1

        print("Aeronave estacionada com sucesso!")

    else:

        if espera == "":
            espera = codigo
            espera_data = tempo_atual

            print("Estacionamento lotado.")
            print("Aeronave colocada na fila de espera.")

        else:
            print("Estacionamento e fila lotados.")
            print("Aeronave enviada para outro aeroporto.")


def retirar_aeronave():
    global caixa
    global total_retiradas
    global espera
    global espera_data
    global total_estacionamentos

    codigo = input("Digite o código da aeronave para retirada: ")

    if codigo not in aeronaves:
        print("Aeronave não encontrada.")
        return

    posicao = aeronaves.index(codigo)

    entrada = datas_entrada[posicao]

    dias = (tempo_atual - entrada).days

    if dias < 1:
        dias = 1

    if dias > 30:
        valor = dias * 115
    else:
        valor = dias * 127

    caixa += valor
    total_retiradas += 1

    print("\nAeronave retirada com sucesso.")
    print("Dias estacionada:", dias)
    print("Valor a pagar: R$", valor)

    aeronaves.pop(posicao)
    datas_entrada.pop(posicao)

    if espera != "":
        aeronaves.append(espera)
        datas_entrada.append(espera_data)

        print("Aeronave da fila de espera entrou no estacionamento.")

        total_estacionamentos += 1

        espera = ""
        espera_data = None


def retirar_todas():
    global espera
    global espera_data

    aeronaves.clear()
    datas_entrada.clear()

    espera = ""
    espera_data = None

    print("Todas as aeronaves foram removidas.")


def mostrar_aeronaves():

    if len(aeronaves) == 0:
        print("Nenhuma aeronave estacionada.")
        return

    print("\nAERONAVES ESTACIONADAS")

    for i in range(len(aeronaves)):
        print(aeronaves[i])

    if espera != "":
        print("\nFila de espera:", espera)


def mostrar_codigo_data():

    if len(aeronaves) == 0:
        print("Nenhuma aeronave estacionada.")
        return

    print("\nCÓDIGO - DATA/HORA DE ENTRADA")

    for i in range(len(aeronaves)):
        print(aeronaves[i], "-", datas_entrada[i])

    if espera != "":
        print("\nFila de espera:")
        print(espera, "-", espera_data)


def adiantar_tempo():
    global tempo_atual

    dias = int(input("Digite quantos dias deseja adiantar: "))
    meses = int(input("Digite quantos meses deseja adiantar: "))

    tempo_atual = tempo_atual + timedelta(days=dias + meses * 30)

    print("Tempo atualizado com sucesso.")


def mostrar_tempo():
    print("\nTempo atual do algoritmo:")
    print(tempo_atual)


def grafico():

    ocupadas = len(aeronaves)
    livres = 5 - ocupadas

    plt.bar(["Ocupadas", "Livres"], [ocupadas, livres])
    plt.title("Vagas do Estacionamento")
    plt.ylabel("Quantidade")
    plt.show()


while True:

    print("\n===== MENU =====")
    print("1 - Solicitar vaga para aeronave")
    print("2 - Retirar aeronave")
    print("3 - Retirar todas as aeronaves")
    print("4 - Mostrar aeronaves presentes")
    print("5 - Mostrar código e data/hora de entrada")
    print("6 - Adiantar o tempo")
    print("7 - Mostrar informações do tempo")
    print("8 - Gráfico")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        solicitar_vaga()

    elif opcao == "2":
        retirar_aeronave()

    elif opcao == "3":
        retirar_todas()

    elif opcao == "4":
        mostrar_aeronaves()

    elif opcao == "5":
        mostrar_codigo_data()

    elif opcao == "6":
        adiantar_tempo()

    elif opcao == "7":
        mostrar_tempo()

    elif opcao == "8":
        grafico()

    elif opcao == "9":

        print("\n===== RELATÓRIO FINAL =====")
        print("Total de estacionamentos realizados:", total_estacionamentos)
        print("Total de retiradas realizadas:", total_retiradas)
        print("Valor total em caixa: R$", round(caixa, 2))

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
