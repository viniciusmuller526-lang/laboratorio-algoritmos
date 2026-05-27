#Crux Sacra Sit Mihi Lux

def calculo_notas ():
    
    soma_notas = 0

    for i in range (0, 5):

        nota = float(input("Insira a nota: "))
        soma_notas += nota
    
    media = soma_notas / 5
    print("A média do aluno é: ", media)
    return media

def aprovado ():

    print ("Aprovado")

def recuperacao ():

    print ("Recuperação")

def reprovado ():

    print ("Reprovado")

def main():

    media = calculo_notas ()

    if media >= 7:

        aprovado()

    elif media < 7 and media >= 4:

        recuperacao()

    else:

        reprovado()

main()
