#Crux Sacra Sit Mihi Lux

def media_notas (nota1, nota2):

    media = (nota1+nota2) / 2
    return media

def aprovacao (media):

    if media >= 7:

        print("Aprovado!")

    else:

        print("Reprovado")

def main():

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = media_notas (n1, n2)
    print("Média: ", media)
    aprovacao(media)

main()
