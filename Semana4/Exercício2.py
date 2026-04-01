#Crux Sacra Sit Mihi Lux

valor_insc = float(input("Digite o valor da incrção: "))

print("1 - A vista")
print("2 - Em 2 vezes")
print("3 - Em 3 vezes")

pagamento = int(input("Digite a opção de pagamento: "))

if pagamento == 2:
    
    parcela = valor_insc / 2
    print("Você pagará 2 parcelas de", parcela, "reais")
    
elif pagamento == 3:
    
    parcela = valor_insc / 3
    print("Você pagará 3 parcelas de", parcela, "reais")
    
else:
    print("Você pagará", valor_insc, "reais")
