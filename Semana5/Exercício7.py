#Crux Sacra Sit Mihi Lux

contador = 0

voto_a = 0
voto_b = 0
voto_c = 0

while contador < 10:
    voto = input("Digite a opção (A - Expresso, B - Cappuccino, C - Chá): ")
    
    if voto == "A":
        voto_a = voto_a + 1
    elif voto == "B":
        voto_b = voto_b + 1
    elif voto == "C":
        voto_c = voto_c + 1
    
    contador = contador + 1

porc_a = (voto_a / 10) * 100
porc_b = (voto_b / 10) * 100
porc_c = (voto_c / 10) * 100

print("Total de votos:")
print("Expresso:", voto_a)
print("Cappuccino:", voto_b)
print("Chá:", voto_c)

print("Porcentagens:")
print("Expresso:", porc_a, "%")
print("Cappuccino:", porc_b, "%")
print("Chá:", porc_c, "%")
