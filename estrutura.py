# tipos primitivos de dados

# int: numeros inteiro
# float: numeros decidmais
# str: cadeia de caracteres
# bool: valores logicos (True ou False)

# operadores aritmeticos: + - * / // % **
# operadores logicos: and or not
# operadores de strings: +, *

# operadores de comparação: ==, !=, >, <, >=, <=

# conversao de tipos
    # x=5.7
    # int(x) # converte pra inteiro == 5
    # str(x) # converte pra string == '5.7'
    # float(x) # converte pra float == 5.7
    # booleanos com dados sao True e se sao nulos ou vazios sao considerados False 

# concatenação de strings
    # 'a' + 'b' == 'ab'
# multiplicacao de strings
    # 'a' * 3 == 'aaa'

# ----------------------

# listas: conjunto de dados ordanos e mutavel
# lista = [1,2,4, 'justo']
# frutas = ['maça', 'banana', 'laranja']
# mista = [1, 'maça', 3.14, True]


# tuplas: conjunto de dados ordenados e imutavel
# coordenada = (5,6)
# tupla = (1,2,4, 'justo')

# dicionarios: co junto de pares na fora de chave e avalor
# pessoa = {
#     'nome': 'João',
#     'idade': 30,
#     'cidade': 'São Paulo'
# }

# conjuntos ou sets: conjuntos de daods nao ordenaos e sem repetição
# c1 = {1,2,3}
# c2 = {3,2,1}
# c3 = {1,2,2,2,2,3}

# s = {1,2,3,4,6,76,42}
# s2 = {4,8,12,16,20}

# s & s2 
    # interseção dos dois conjuntos
    # {4}

# s | s2 
    # uniao dos conjuntos
    # {1,2,3,4,6,76,42,8,12,16,20}

# s - s2
    # diferença dos conjuntos
    # {1, 2, 3, 6, 42, 76}

# ---------------------------

#  pessoa = { 'nome' : 'joao', 'idade': 18 } 
#  pessoa
# {'nome': 'joao', 'idade': 18}
#  pessoa['nome']  
# 'joao'

# posso tambem trocar o dados
#  pessoa['nome'] = 'pedro'
#  pessoa
# {'nome': 'pedro', 'idade': 18}

# adicionar dados ao dicionario
# pessoa['cpf'] = '123.542.780-10'
# 'nome': 'pedro', 'idade': 18, 'cpf': '123.542.780-10'}