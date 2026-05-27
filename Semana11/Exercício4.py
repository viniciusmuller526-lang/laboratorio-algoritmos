#Crux Sacra Sit Mihi Lux

def valor_pagar (total_laranjas):

    if total_laranjas >= 12:

        valor = total_laranjas * 0.25
        return valor


    else:

        valor = total_laranjas * 0.40
        return valor


def main():

    total_laranjas = int(input("Insira o total de laranjas que deseja comprar: "))
    valor = valor_pagar(total_laranjas)
    print("O valor a ser pago é: ", valor, "reais")

main()
