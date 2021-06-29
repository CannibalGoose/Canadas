# Esse é o arquivo modificado, contendo 
# alterações com viés de programação orientada
# à objeto

# A programação orientada a objetos ajuda o projeto
# a se manter sobre controle, em caso de aumento
# considerável de escala (acredite, as coisas crescem muito)

from Classes.Contador import Contador

# aqui em cima, com 'from...', você importa objetos e funções
# de outras bibliotecas e scripts
# isso é muito usado o tempo inteiro, acostume-se a isso

# Na pasta 'Classes' está a classe criada 'Contador' que 
# possui as funções que não estão mais descritas aqui, no Main. 
# O script 'Contador.py' cumpre a função de ter mais código 
# escrito, com funções e variáveis prórpias, 
# que não poluem o principal script de trabalho

def main():
    citacao = input("Coloque aqui a frase para ser lida: ")
    print("\nMenu")
    print("1. Contar o número de vogais no texto ingressado.")
    print("2. Contar o número de maiúsculas no texto ingressado.")
    escolha = int(input("Selecione 1 ou 2 do menu: "))
    if escolha == 1:
        print("Número de vogais: ", Contador.calcularNumeroDeVogais(citacao))
    else:
        print("Número de maiúsculas: ", Contador.calcularNumeroDeMaiusculas(citacao))

main()

# Você pode notar que o programa funciona
# exatamente como funcionava
# anteriormente, mas agora, com 
# o script 'main' muito mais enxuto