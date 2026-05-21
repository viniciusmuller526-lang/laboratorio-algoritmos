#Crux Sacra Sit Mihi Lux

valores = []
n = 10
quant_valores_maiores_100 = 0


for i in range (n):

    valor = float(input("Insira um valor: "))
    valores.append(valor)

    if valor > 100:

        quant_valores_maiores_100 += 1

print("Quantidade de valores maiores que 100: ", quant_valores_maiores_100)
print("Valores maiores que 100:")

for i in range (len(valores)):

    if valores[i] > 100:

        print("Valor", i + 1, "=", valores[i])
