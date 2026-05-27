#Crux Sacra Sit Mihi Lux

def soma_imposto (taxa_imposto, custo):

    taxa_soma = (custo * taxa_imposto / 100) + custo
    return taxa_soma

def main():

    taxa_imposto = float(input("Insira a taxa: "))
    custo = float(input("Insira o custo do produto: "))
    taxa_soma = soma_imposto(taxa_imposto, custo)
    print("O valor após a aplicação da taxa é: ", taxa_soma)

main()
