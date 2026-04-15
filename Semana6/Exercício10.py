#Crux Sacra Sit Mihi Lux

valor_oliveiras = 13
valor_usuario = 0

while valor_usuario != 14:

    valor_usuario = int(input("Adivinhe o número de 1 a 100: "))

    if valor_usuario < valor_oliveiras:

        print("Há mais oliveiras, tente um número maior")

    elif valor_usuario > valor_oliveiras:

        print("Há menos oliveiras, tente um número menor")

print("Parabéns, você descobriu a quantidade de oliveiras!")
