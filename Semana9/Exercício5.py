#Crux Sacra Sit Mihi Lux

mulheres = 0
homens = 0

olho_a = 0
olho_v = 0
olho_c = 0

cabelo_l = 0
cabelo_c = 0
cabelo_p = 0

entre_18_35_olho_v_cabelo_preto = 0

maior_idade = 0


for contador in range (15):

    print("Sexo")
    print("f - feminino")
    print("m - masculino")
    sexo = input("Insira a letra correspondente a seu sexo: ")
    
    if sexo == "f":

        mulheres += 1

    elif sexo == "m":

        homens += 1
      
    print("Cor dos olhos")
    print("a - azul")
    print("v - verde")
    print("c - castanho")
    cor_olhos = input("Insira a letra correspondente a cor dos seus olhos: ")

    if cor_olhos == "a":

        olho_a += 1
        
    elif cor_olhos == "v":

        olho_v += 1

    elif cor_olhos == "c":

        olho_c += 1


    print("Cor do cabelo")
    print("l - loiro")
    print("c - castanho")
    print("p - preto")
    cor_cabelo = input("Insira a letra correspondente a cor do seu cabelo: ")

    if cor_cabelo == "l":

        cabelo_l += 1

    elif cor_cabelo == "c":

        cabelo_c += 1
    
    elif cor_cabelo == "p":

        cabelo_p += 1

    idade = int(input("Agora insira sua idade: "))

    if contador == 0:

        maior_idade = idade

    elif idade > maior_idade:

        maior_idade = idade
    
    if idade >= 18 and idade <= 35 and cor_olhos == "v" and cor_cabelo == "p":

        entre_18_35_olho_v_cabelo_preto += 1



porcent_mulheres = (mulheres / 15) * 100
porcent_homens = (homens / 15) * 100

porcent_olho_a = (olho_a / 15) * 100
porcent_olho_v  = (olho_v / 15) * 100
porcent_olho_c = (olho_c / 15) * 100

porcent_cabelo_l = (cabelo_l / 15) * 100
porcent_cabelo_c = (cabelo_c / 15) * 100
porcent_cabelo_p = (cabelo_p / 15) * 100

print("A maior idade do grupo é: ", maior_idade, "anos")
print("Há", entre_18_35_olho_v_cabelo_preto, "pessoas entre 18 e 35 anos com olhos verdes e cabelos pretos.")
print("Porcentagem de mulheres: ", porcent_mulheres, "%")
print("Porcentagem de homens: ", porcent_homens, "%")
print("Porcentagem de pessoas com olhos azuis: ", porcent_olho_a, "%")
print("Porcentagem de pessoas com olhos verdes: ", porcent_olho_v, "%")
print("Porcentagem de pessoas com olhos castanhos: ", porcent_olho_c, "%")
print("Porcentagem de pessoas com cabelo loiro: ", porcent_cabelo_l, "%")
print("Porcentagem de pessoas com cabelo castanho: ", porcent_cabelo_c, "%")
print("Porcentagem de pessoas com cabelo preto: ", porcent_cabelo_p, "%")
