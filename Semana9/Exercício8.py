#Crux Sacra Sit Mihi Lux

dent_intervalo = 0
fora_intervalo = 0

for contador in range (10):

    numero = int(input("Insira um número: "))

    if numero > 10 and numero < 20:

        dent_intervalo += 1

    else:

        fora_intervalo += 1

print("Há", dent_intervalo, "números dentro do intervalo entre 10 e 20 e", fora_intervalo, "números fora do intervalo")
