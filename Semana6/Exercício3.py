#Crux Sacra Sit Mihi Lux

oliveiras = int(input("Digite a quantia de oliveiras a serem plantadas: "))
fileiras = int(input("Digite o total de fileiras: "))

divisao = oliveiras / fileiras
sobra = oliveiras % fileiras

print("O número de mudas em cada fileira será",(int(divisao)))
print("O número de mudas a sobrar é",sobra)
