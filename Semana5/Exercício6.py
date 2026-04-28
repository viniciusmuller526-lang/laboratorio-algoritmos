#Crux Sacra Sit Mihi Lux

contador = 0
entre_15_25 = 0

while contador < 10:
    temperatura = float(input("Digite a temperatura da cidade: "))
    
    if temperatura >= 15 and temperatura <= 25:
        entre_15_25 = entre_15_25 + 1
    
    contador = contador + 1

print("Quantidade de cidades com temperatura entre 15°C e 25°C:", entre_15_25)
