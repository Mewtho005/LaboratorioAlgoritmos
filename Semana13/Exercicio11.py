import random

def main():
    lotes = []
    pares = 0
    impares = 0

    for i in range(10):
        id = random.randint(1, 50)
        lotes.append(id)

        if id % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("IDs dos lotes:")
    print(lotes)

    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)

main()
