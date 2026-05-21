#Crux Sacra Sit Mihi Lux

numeros = []
num_maior_30 = 0
soma_num_maior_30 = 0
n = 8

for i in range (n):

    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range (len(numeros)):

    print("-", numeros[i])

for i in range (len(numeros)):

    if numeros [i] > 30:

        num_maior_30 += 1
        soma_num_maior_30 += numeros[i]

soma = sum(numeros)


print("Quatidade de números maiores que 30: ", num_maior_30)
print("Soma dos números maiores que 30: ", soma_num_maior_30)
print("Soma total dos números: ", soma)
