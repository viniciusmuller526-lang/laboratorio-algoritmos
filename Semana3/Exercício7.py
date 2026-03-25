# Cruz Sacra Sit Mihi Lux

altura = float (input ("Digite sua altura: "))
sexo = input ("Digite seu sexo:").upper()

if sexo == "M":
    
    peso = (72.7*altura) - 58
    print("Seu peso ideal é:", peso)
    
else:
    if sexo == "F":
    
        peso = (62.1*altura) - 44.7
        print("Seu peso ideal é:", peso)

    else:
        
        print("Erro")
