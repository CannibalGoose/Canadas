# Esse é o arquivo original, contendo 
# apenas correções simples na acentuação


def main():
    citacao = input("Coloque aqui a frase para ser lida: ")
    print("\nMenu")
    print("1. Contar o número de vogais no texto ingressado.")
    print("2. Contar o número de maiúsculas no texto ingressado.")
    escolha = int(input("Selecione 1 ou 2 do menu: "))
    if escolha == 1:
        print("Número de vogais: ", calcularNumeroDeVogais(citacao))
    else:
        print("Número de maiúsculas: ", calcularNumeroDeMaiusculas(citacao))

def calcularNumeroDeVogais(citacao):
    numeroDeVogais = 0
    for ch in citacao:
        if ch.upper() in "AEIOU":
            numeroDeVogais += 1
    return numeroDeVogais

def calcularNumeroDeMaiusculas(citacao):
    numeroDeMaiusculas = 0
    for ch in citacao:
        if ('A' <= ch <= 'Z'):
            numeroDeMaiusculas += 1
    return numeroDeMaiusculas

main()