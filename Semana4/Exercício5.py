#Crux Sacra Sit Mihi Lux

print("Se desejar, escolha um dos kits abaixo: ")
print("1 → Kit Básico: Número de peito + medalha - R$100,00")
print("2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00")
print("3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00")

opcao = int(input("Digite sua escolha de kit: "))
pagamento = float(input("Insira o valor que pagará: "))

if opcao == 1:
    
    if pagamento >= 100:
        
        troco = pagamento - 100
        print("Seu pagamento foi efetivado! Você receberá o kit 1 e", troco, "reais de troco.")
        
    else:
        
        print("Pagamento insuficiente :(")

elif opcao == 2:
    
    if pagamento >= 120:
        
        troco = pagamento - 120
        print("Seu pagamento foi efetivado! Você receberá o kit 2 e", troco, "reais de troco.")
        
    else:
        
        print("Pagamento insuficiente :(")
        
elif opcao == 3:
    
    if pagamento >= 150:
        
        troco = pagamento - 150
        print("Seu pagamento foi efetivado! Você receberá o kit 3 e", troco, "reais de troco.")
        
    else:
        
        print("Pagamento insuficiente :(")
    
else:
    
    print("Opcão inválida :(")
