#Crux Sacra Sit Mihi Lux

litros_agua = 500
ciclo_irrig = 30
contador = 0

while litros_agua > 0:

    litros_agua = litros_agua - ciclo_irrig
    contador += 1

print("Foram realizados",contador,"ciclos")
