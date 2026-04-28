#Crux Sacra Sit Mihi Lux

ingressos = 100
opcao = 0

while opcao != 4:

    print("1 - Vender ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:

        quantidade = int(input("Quantos ingressos deseja comprar?: "))
        ingressos = ingressos - quantidade
    
    elif opcao == 2:

        extras = int(input("Digite a quantidade de ingressos a adicionar: "))
        ingressos = ingressos + extras

    elif opcao == 3:

        print("Ainda há", ingressos, "ingressos restantes")

    elif opcao == 4:

        print("Processo finalizado :)")

    else:

        print("Opção inválida :(")
