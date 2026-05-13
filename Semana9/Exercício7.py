#Crux Sacra Sit Mihi Lux

inicio = int(input("Digite um número inteiro: "))
fim = int(input("Digite um número inteiro maior que o anterior: "))

for numero in range(inicio, fim):

    
    if numero % 2 == 0:

        print("-", numero)
