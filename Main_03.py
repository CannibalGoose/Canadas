# Esse é o arquivo modificado, 
# contendo a função que retornaria ao 
# começo do main loop, e não encerra o programa

# Aqui tentamos prever um possível input errado do usuário
# um aproach bom pra essa hora seria o 'try' e 'except'
# mas isso tu que tem que pesquisar, papai

# Nessa versão o programa só se encerra 
# quando dizemos para ele encerrar

def main():
    citacao = input("\nColoque aqui a frase para ser lida: ")
    print("\nMenu")
    print("1. Contar o número de vogais no texto ingressado.")
    print("2. Contar o número de maiúsculas no texto ingressado.")
    escolha = int(input("Selecione 1 ou 2 do menu: "))
    if escolha == 1:
        print("\nNúmero de vogais: ", calcularNumeroDeVogais(citacao))
    elif escolha == 2:
        print("\nNúmero de maiúsculas: ", calcularNumeroDeMaiusculas(citacao))
    else:
        print("\n\nERRO: '" +str(escolha)+ "' não é compatível com as opções!\n\n")
        main()
    checarSeContinua()

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

def checarSeContinua():
    print("\nMenu")
    print("1. Retornar ao início e inserir uma nova frase.")
    print("2. Encerrar o programa.")
    escolha = int(input("Selecione 1 ou 2 do menu: "))
    if escolha == 1:
        print("\n--RETORNAR--\n")
        main()
    elif escolha == 2:
        print("\n--ENCERRAR--\n")
        quit()
    else:
        print("\n\nERRO: '" +str(escolha)+ "' não é compatível com as opções!\n\n")
        checarSeContinua()


main()