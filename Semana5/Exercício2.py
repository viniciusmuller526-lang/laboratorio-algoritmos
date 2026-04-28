#Crux Sacra Sit Mihi Lux

carrinho = 0

codigo = 1

while codigo != 0:

    codigo = int(input("Digite o código do produto: "))

    if codigo == 1040:

        carrinho = carrinho + 1
        
    elif codigo == 0:
        
        print("Quantidade de vezes que o código 1040 foi digitado: ", carrinho)
        print("Processo encerrado :)")
