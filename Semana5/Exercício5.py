#Crux Sacra Sit Mihi Lux

contador = 0
maiores_18 = 0

while contador < 10:
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade >= 18:
        maiores_18 = maiores_18 + 1
    
    contador = contador + 1

print("Quantidade de pessoas com 18 anos ou mais:", maiores_18)
