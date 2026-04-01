#Crux Sacra Sit Mihi Lux

valor_ing = float(input("Insira o valor do ingresso:"))

print("1 - Ingresso normal (valor cheio)")
print("2 - Estudante (50% de desconto")
print("3 - Criança até 12 anos (60% de desconto)")
print("4 - Idoso (40% de desconto)")

ingresso = int(input("Insira o tipo de ingresso: "))

if ingresso == 1:
    
    print("Você pagará", valor_ing, "reais")
    
elif ingresso == 2:
    
    valor_final = valor_ing * 0.5
    print("Você pagará", valor_final, "reais")
    
elif ingresso == 3:
    
    valor_final = valor_ing * 0.4
    print("Você pagará", valor_final, "reais")

elif ingresso == 4:
    
    valor_final = valor_ing * 0.6
    print("Você pagará", valor_final, "reais")
    
else:
    
    print("Opção inválida :(")
