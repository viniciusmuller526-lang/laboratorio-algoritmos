#Crux Sacra Sit Mihi Lux

def dobro (valor):

    valor_dobro = valor * 2
    print("O dobro desse valor é: ", valor_dobro)

def triplo (valor):

    valor_triplo = valor * 3
    print("O triplo desse valor é: ", valor_triplo)

def main():

    valor = float(input("Insira um valor: "))
    dobro(valor)
    triplo(valor)
    
main()
