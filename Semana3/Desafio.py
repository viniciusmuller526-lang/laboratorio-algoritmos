# Cruz Sacra Sit Mihi Lux

nome = input ("Insira seu nome:")
valor_compra = float (input ("Insira o valor de sua compra:"))
pagamento = int (input ("Insira a forma de pagamento:"))

if valor_compra > 200:
    if pagamento == 1:
        valor_compra = valor_compra * 0.85
        print("Sua compra deu:", valor_compra, "reais")
    
    else:
        valor_compra = valor_compra * 0.95
        print("Sua compra deu:", valor_compra, "reais")
else:
    if valor_compra <= 200:
        valor_compra = valor_compra * 0.9
        print("Sua compra deu:", valor_compra, "reais")
    
    else:
        print("Sua compra deu:", valor_compra, "reais")
