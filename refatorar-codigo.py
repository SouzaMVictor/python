def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    return "aprovado" if media >= 6 else "reprovado"

nota1 = 7
nota2 = 4
media = calcular_media(nota1, nota2)
print(f"Status: {verificar_aprovacao(media)} Média: {media}")

nota3 = 8
nota4 = 9
media2 = calcular_media(nota3, nota4)
print(f"Status: {verificar_aprovacao(media2)} Média: {media2}")

#codigo redundante
#vamos melhorar
