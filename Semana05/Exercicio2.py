forca1 = float(input("Digite a primeira força: "))
forca2 = float(input("Digite a segunda força: "))
forca3 = float(input("Digite a terceira força: "))

if (forca1 + forca2 > forca3) and (forca1 + forca3 > forca2) and (forca2 + forca3 > forca1):
    if forca1 == forca2 == forca3:
        print("Equilíbrio simétrico")
    elif forca1 == forca2 or forca1 == forca3 or forca2 == forca3:
        print("Equilíbrio parcialmente simétrico")
    else:
        print("Equilíbrio assimétrico")
else:
    print("Não há equilíbrio")
