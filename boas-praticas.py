# def f(n):
#     x = sum(n) / len(n)
#     if x >= 6:
#         print("aprovado")
#     else:
#         print("reprovado")

#usar nomes descritivos - facilita leitura de codigo

def calcula_media(notas):
    media = sum(notas) / len(notas)
    if media >= 6:
        print("aprovado")
    else:
        print("reprovado")