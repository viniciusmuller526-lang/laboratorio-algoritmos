#Crux Sacra Sit Mihi Lux

contador = 0
maior = 0
menor = 0
olivas = 0
dia_maior = 0
dia_menor = 0

while contador != 7:

    olivas_dia = int(input("Digite a quantia de oliveiras colhidas hoje: "))

    if contador == 0:

            maior = olivas_dia
            menor = olivas_dia

    if olivas_dia > maior:
        
            maior = olivas_dia
            dia_maior = contador + 1

    elif olivas_dia < menor:
    
            menor = olivas_dia
            dia_menor = contador + 1

    olivas = olivas + olivas_dia
    contador += 1
    

print("Total de olivas colhidas essa semana: ",olivas)
print("O dia de maior colheita foi o dia",dia_maior)
print("O dia de menor colheita foi o dia",dia_menor)
