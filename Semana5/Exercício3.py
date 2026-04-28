#Crux Sacra Sit Mihi Lux

contador = 0
soma = 0

menos_30 = 0
entre_30_60 = 0

while contador < 7:
    tempo = float(input("Digite o tempo do corredor: "))
    
    soma = soma + tempo
    
    if tempo < 30:
        menos_30 = menos_30 + 1
    elif tempo <= 60:
        entre_30_60 = entre_30_60 + 1
    
    contador = contador + 1

media = soma / 7

porcentagem = (entre_30_60 / 7) * 100

print("Tempo médio:", media)
print("Corredores com menos de 30 minutos:", menos_30)
print("Porcentagem entre 30 e 60 minutos:", porcentagem, "%")
