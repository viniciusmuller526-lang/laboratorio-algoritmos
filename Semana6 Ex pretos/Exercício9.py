#Crux Sacra Sit Mihi Lux

idade = int(input('Digite sua idade: '))

while idade <= 0 or idade >= 150:

    print('Erro, tente de novo')
    idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salário: '))

while salario <= 0:

    print('Erro, tente de novo')
    salario = float(input('Digite seu salário: '))

sexo = input('Digite seu sexo: ')

while sexo != 'f' and sexo != 'm':

    print('Erro, tente de novo')
    sexo = input('Digite seu sexo: ')

print('Estado Civil')
print('s - solteiro')
print('c - casado')
print('v - viúvo')
print('d- divorciado')

estcivil = input('Digite a letra correspondente a seu atual estado civil: ')

while estcivil != 's' and estcivil != 'c'and estcivil != 'v' and estcivil != 'd':

    print('Erro, tente de novo')
    estcivil = input('Digite a letra correspondente a seu atual estado civil: ')

print('Informações válidadas :)')
