#Crux Sacra Sit Mihi Lux

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:

    print("Nota 1:",nota1)
    print("Nota 2:",nota2)
    print("Média",media)
    print("Conceito A - Aprovado")

elif media >= 7.5 and media <= 9:

    print("Nota 1:",nota1)
    print("Nota 2:",nota2)
    print("Média",media)
    print("Conceito B - Aprovado")

elif media >= 6 and media <= 7.5:

    print("Nota 1:",nota1)
    print("Nota 2:",nota2)
    print("Média",media)
    print("Conceito C - Aprovado")

elif media >= 4 and media <= 6:

    print("Nota 1:",nota1)
    print("Nota 2:",nota2)
    print("Média",media)
    print("Conceito D - Reprovado")

elif media >= 0 and media <= 4:

    print("Nota 1:",nota1)
    print("Nota 2:",nota2)
    print("Média",media)
    print("Conceito E - Reprovado")

