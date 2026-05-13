#Crux Sacra Sit Mihi Lux

quant_pares = 0
quant_impares = 0
quant_zeros = 0


for contador in range(10):

    resp = int(input("Digite um número inteiro:"))

    if resp == 0:

        quant_zeros += 1

    elif resp % 2 == 0:

        quant_pares += 1

    else:

        quant_impares += 1

print("A quantia de números ímpares é: ", quant_impares)
print("A quantia de números pares é: ", quant_pares)
print("A quantidade de zeros é: ", quant_zeros)
