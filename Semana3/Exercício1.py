horas = float(input("Coloque suas horas trabalhadas: "))

salario = horas * 35

if salario < 1000:
    
    salario = salario + 300
    print("Seu salário é", salario, "reais")
    
else:
    
    print("Seu salário é", salario, "reais")
