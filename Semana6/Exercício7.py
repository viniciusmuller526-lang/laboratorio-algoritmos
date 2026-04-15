#Crux Sacra Sit Mihi Lux

contador = 0
idade_total = 0

while contador != 15:

    idade = int(input("Digite sua idade: "))
    idade_total = idade_total + idade
    contador += 1

media = idade_total / 15

if media >= 0 and media <= 25:

    print("A média de idade é", (int(media)), "anos")
    print("Turma Jovem")

elif media >= 26 and media <= 60:

    print("A média de idade é", (int(media)), "anos")
    print("Turma Adulta")

elif media > 60:

    print("A média de idade é", (int(media)), "anos")
    print("Turma Idosa")
