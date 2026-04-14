#Crux Sacra Sit Mihi Lux

afirmativas = 0

print("")
print("1 - Sim")
print("2 - Não")

resposta1 = int(input("Digite sua resposta: "))

if resposta1 == 1:

    afirmativas += 1

print("")
print("1 - Sim")
print("2 - Não")

resposta2 = int(input("Digite sua resposta: "))

if resposta2 == 1:

    afirmativas += 1

print("")
print("1 - Sim")
print("2 - Não")

resposta3 = int(input("Digite sua resposta: "))

if resposta3 == 1:

    afirmativas += 1

print("")
print("1 - Sim")
print("2 - Não")

resposta4 = int(input("Digite sua resposta: "))

if resposta4 == 1:

    afirmativas += 1

print("")
print("1 - Sim")
print("2 - Não")

resposta5 = int(input("Digite sua resposta: "))

if resposta5 == 1:

    afirmativas += 1

if afirmativas == 2:

    print("Se treinar mais vai")

elif afirmativas > 2 and afirmativas < 5:

    print("Competitivo")

elif afirmativas == 5:

    print("Já ganhou!!!")

else:

    print("Fica no banco msm")
