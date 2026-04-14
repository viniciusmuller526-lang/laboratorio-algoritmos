#Crux Sacra Sit Mihi Lux

litros = float(input("Insira a quantidade de litros: "))
valor = float(input("Insira o valot total: "))

if litros >= 20 and valor > 100:

    valor = valor * 0.9
    print("Você receberá 10 porcento de desconto e pagará", valor,"reais")

elif litros >= 20 and valor <= 100:

    valor = valor *0.95
    print("Você receberá 5 porcento de desconto e pagará",valor,"reais")

else:

    print("Você pagará",valor,"reais")
