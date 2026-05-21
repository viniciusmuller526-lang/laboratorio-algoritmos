#Crux Sacra Sit Mihi Lux

vetor = []

opcao = 0

while opcao != 5:

    print("")
    print("--- MENU VETOR ---")
    print("")
    print(vetor)
    print("")
    print("1 - Inserir Item")
    print("2 - Retirar Item")
    print("3 - Listar Itens")
    print("4 - Retirar Todos os Itens")
    print("5 - Sair")
    print("")

    opcao = int(input("Escolha uma ação: "))

    if opcao == 1:

        valor = float(input("Insira o valor a ser inserido: "))
        vetor.append(valor)

    
    elif opcao == 2:

        pos = int(input("Insira a posição do item que deseja remover: "))
        vetor.pop(pos - 1)

    elif opcao == 3:

        print("")
        print("Lista dos itens: ")

        for i in range (len(vetor)):

            print("Item", i + 1, "=", vetor[i])

    elif opcao == 4:

        vetor = []
