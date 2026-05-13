#Crux Sacra Sit Mihi Lux

num_anterior = 1
numero = 1
fibonacci = 0

print(fibonacci)
print(num_anterior)
print(numero)
for contador in range (7):
    
    fibonacci = num_anterior + numero
    num_anterior = numero
    numero = fibonacci
    
    print(fibonacci)
