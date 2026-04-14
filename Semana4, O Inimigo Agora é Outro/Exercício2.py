#Crux Sacra Sit Mihi Lux

forca1 = float(input("Digite o valor da primeira força: "))
forca2 = float(input("Digite o valor da segunda força: "))
forca3 = float(input("Digite o valor da terceira força: "))

if forca1 + forca2 > forca3 and forca2 + forca3 > forca1 and forca3 + forca1 > forca2:

    if forca1 == forca2 and forca2 == forca3 and forca3 == forca1:

        print("Equilíbrio Simétrico")

    elif forca1 == forca2 or forca2 == forca3 or forca3 == forca1:

        print("Equilíbrio Parcialmente Simétricco")

    else:

        print("Equilíbrio Asssimétrico")

else:

    print("Não há equilíbrio")
