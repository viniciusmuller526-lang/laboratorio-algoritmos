#Crux Sacra Sit Mihi Lux

vetor_a = []
n = 10

for i in range (n):

    valor = float(input("Insira um valor: "))
    vetor_a.append(valor)

vetor_b = []

for i in range (len(vetor_a)):

    vetor_b.append(vetor_a[(-i + -1)])

print("Vetor A: ", vetor_a)
print("Vetor B: ", vetor_b)
