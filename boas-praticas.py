# def f(n):
#     x = sum(n) / len(n)
#     if x >= 6:
#         print("aprovado")
#     else:
#         print("reprovado")

#usar nomes descritivos - facilita leitura de codigo

# def calcula_media(notas):
#     media = sum(notas) / len(notas)
#     if media >= 6:
#         print("aprovado")
#     else:
#         print("reprovado")

#geralmente usa-se verbo no infinitivo para nome de funcoes

# def calcular_media(notas):
#     media = sum(notas) / len(notas)
#     if media >= 6:
#         print("aprovado")
#     else:
#         print("reprovado")

#snake_case = funçoes e variaveis 
#camelCase = nao usado em python
#PascalCase = recomednado parar classes em python
#kebab-case = nao usado em python, acha que é subtração
#SCREAMING_SNAKE_CASE = usado para constantes

#separar conceitos em funcoes diferentes. dividir responsabilidades

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "aprovado"
    else:
        return "reprovado"
