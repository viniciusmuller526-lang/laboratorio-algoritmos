#Crux Sacra Sit Mihi Lux

time1 = int(input("Coloque a pontuação do Time 1: "))
time2 = int(input("Coloque a pontuação do Time 2: "))

if time1 > time2:
    
    print("Time 1 venceu e 2 perdeu")
    
elif time1 < time2:
    
    print("Time 2 venceu e 1 perdeu")
    
else:
    print("Empate")
