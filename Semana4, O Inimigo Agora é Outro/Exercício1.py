#Crux Sacra Sit Mihi Lux

nome = input("Insira seu nome: ")
salario = float(input("Insira seu salário atual: "))
anos = int(input("A quantos anos você trabalha na equipe?: "))

if anos >= 5 and salario <= 2000:

    salario = salario * 1.1

    print(nome)
    print("Você recebeu um aumento de 10 porcento e receberá", salario, "reais por mês")

else:

    salario = salario * 1.05

    print(nome)
    print("Você recebeu um aumento de 5 porcento e receberá", salario, "reais por mês")
