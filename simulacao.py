# se jogar dois dados mil veszes quantas, vezes dara a soma 7?

import random

# numero_de_vezes = 0

# for _ in range (1000):
#     dado1 =  random.randint(1,6)
#     dado2 =  random.randint(1,6)
#     soma = dado1 + dado2
#     if soma == 7:
#         numero_de_vezes += 1

# print(f'a soma dos dados deu 7 {numero_de_vezes} vezes')


# sorteador de numeros da mega sena
numeros_sorteados = []
while len(numeros_sorteados) < 6:
    numero = random.randint(1,60)
    if numero not in numeros_sorteados:
        numeros_sorteados.append(numero)

print(numeros_sorteados)