#Crux Sacra Sit Mihi Lux

plantA = 80000
plantB = 200000
anos = 0

while plantA <= plantB:

    plantA = plantA * 1.03
    plantB = plantB * 1.015
    anos += 1

print("Levaram",anos,"para a plantação A ultrapassar a plantação B")
