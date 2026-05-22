def menu():
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = float(input("Opção: "))
    return opcao

def mostrarsaldo(saldo):
    print("Saldo atual", saldo)

def sacar(saldo):
    valor = float(input("Digite um valor para saque: "))
    if valor <= saldo:
        saldo -= valor
        mostrarsaldo(saldo)
    else:
        print("Saldo insuficiente")
    return saldo

def depositar(saldo):
    valor = float(input("Valor para de deposito: "))
    saldo += valor
    mostrarsaldo(saldo)
    return saldo

def main():
    saldo = 0
    opcao = 0

    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            mostrarsaldo(saldo)
main()
