import random

def main():
    lotes = []

    for i in range(10):
        lotes.append(random.randint(1, 100))

    print("IDs dos lotes:")
    print(lotes)

    print("IDs pares:")
    for id in lotes:
        if id % 2 == 0:
            print(id)

main()
