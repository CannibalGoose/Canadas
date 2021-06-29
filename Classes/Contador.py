class Contador:
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