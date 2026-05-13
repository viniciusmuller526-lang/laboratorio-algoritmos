#Crux Sacra Sit Mihi Lux

a = 0
b = 0
c = 0

for contador in range (20):

    print("a - Jornal A")
    print("b - Jornal B")
    print("c - Jornal C")

    resp = input("Insira a letra correspondente ao seu jornal favorito: ")
    
    if resp == "a":

        a += 1

    elif resp == "b":

        b += 1

    elif resp == "c":

        c += 1

porcent_a = (a / 20) * 100
porcent_b = (b / 20) * 100
porcent_c = (c / 20) * 100

if a >= b and a >= c:

    if b >= c:

        print("Jornal C: ", porcent_c, "%")
        print("Jornal B: ", porcent_b, "%")
        print("Jornal A: ", porcent_a, "%")
    
    else:

        print("Jornal B: ", porcent_b, "%")
        print("Jornal C: ", porcent_c, "%")
        print("Jornal A: ", porcent_a, "%")

elif b >= a and b >= c:

    if a >= c:

        print("Jornal C: ", porcent_c, "%")
        print("Jornal A: ", porcent_a, "%")
        print("Jornal B: ", porcent_b, "%")
    
    else:

        print("Jornal A: ", porcent_a, "%")
        print("Jornal C: ", porcent_c, "%")
        print("Jornal B: ", porcent_b, "%")

elif c >= a and c >= b:

    if a >= b:

        print("Jornal B: ", porcent_b, "%")
        print("Jornal A: ", porcent_a, "%")
        print("Jornal C: ", porcent_c, "%")
    
    else:

        print("Jornal A: ", porcent_a, "%")
        print("Jornal B: ", porcent_b, "%")
        print("Jornal C: ", porcent_c, "%")
