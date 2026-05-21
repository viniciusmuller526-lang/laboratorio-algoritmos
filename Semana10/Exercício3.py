#Crux Sacra Sit Mihi Lux

valores = []
n = 10

for i in range (n):

    valor = float(input("Insira um valor: "))
    valores.append(valor)

print("Valores pares e suas posições: ")

for i in range (len(valores)):

    if valores[i] % 2 == 0:

        print("Valor", i + 1, "=", valores[i])
