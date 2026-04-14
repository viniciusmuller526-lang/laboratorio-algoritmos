#Crux Sacra Sit Mihi Lux

morango = 0
maca = 0
kg_morango = float(input("Digite a quantia de kg de morango que deseja comprar: "))
kg_maca = float(input("Digite a quantia de kg de maçã que deseja comprar: "))


if kg_morango <= 5:

    morango = 2.5

else:

    morango = 2.2

if kg_maca <= 5:

    maca = 1.8

else:

    maca = 1.5

if kg_morango > 8 or morango > 25:

    morango = morango * 0.9

if kg_maca > 8 or maca > 25:

    maca = maca * 0.9

valor = morango + maca

print(valor)
