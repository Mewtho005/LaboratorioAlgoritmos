def converterHora(hora, minuto):
    if hora == 0:
        novaHora = 12
        periodo = "A.M."
    elif hora < 12:
        novaHora = hora
        periodo = "A.M."
    elif hora == 12:
        novaHora = 12
        periodo = "P.M."
    else:
        novaHora = hora - 12
        periodo = "P.M."
    
    return novaHora, minuto, periodo

def mostrarHora(hora, minuto, periodo):
    print(hora, ":", minuto, periodo)

def main():
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))
    
    if hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59:
        h, m, p = converterHora(hora, minuto)
        mostrarHora(h, m, p)
    else:
        print("Horario invalido")

main()
