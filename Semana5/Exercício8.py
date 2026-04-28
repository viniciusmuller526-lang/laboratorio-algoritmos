#Crux Sacra Sit Mihi Lux

caixa = float(input("Insira a quantia de dinheiro em caixa:"))
opcao = 0

while opcao != 4:

    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Mostrar dinheiro em caixa")
    print("4 - Encerrar")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:

        venda = int(input("Insira o valor da venda: "))
        caixa = caixa + venda
    
    elif opcao == 2:

        saque = int(input("Digite a quantia de dinheiro que deseja sacar: "))
        caixa = caixa - saque

    elif opcao == 3:

        print("Ainda há", caixa, "reais em caixa")

    elif opcao == 4:

        print("Processo finalizado :)")

    else:

        print("Opção inválida :(")
