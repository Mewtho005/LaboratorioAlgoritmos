idade = int(input("Digite a idade da oliveira em anos: "))

altura = idade * 30

print("Altura estimada:", altura, "cm")

if altura > 500:
    print("Oliveira adulta")
else:
    print("Oliveira em crescimento")
