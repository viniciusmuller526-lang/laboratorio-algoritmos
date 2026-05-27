#Crux Sacra Sit Mihi Lux

def conversao (hora_antiga, minutos):

    if hora_antiga < 12:

        hora_nova = hora_antiga
        periodo = "AM"
        return hora_nova, minutos, periodo
    
    elif hora_antiga >= 13 and hora_antiga <= 23:

        hora_nova = hora_antiga - 12
        periodo = "PM"
        return hora_nova, minutos, periodo
    
    elif hora_antiga == 12:

        hora_nova = hora_antiga
        periodo = "PM"
        return hora_nova, minutos, periodo
    

def saida (hora_nova, minutos, periodo):

    
    print("São: ", hora_nova, ":", minutos, periodo)


def main():

    hora = int(input("Insira a hora: "))
    minutos = int(input("Insira os minutos: "))
    hora_nova, minutos, periodo = conversao(hora, minutos)
    saida(hora_nova, minutos, periodo)

main()
