def somar_maiores(lista, limite, multiplicador): 
    resultado = [] 
    soma_maiores = 0

    for elemento in lista:
        if elemento > limite: 
            soma_maiores += elemento
            resultado.append(elemento * multiplicador)

    print("soma:", soma_maiores)
    print("lista:", resultado)

somar_maiores([10, 20, 30, 40, 50], 35, 2)
