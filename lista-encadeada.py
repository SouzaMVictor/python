lista = None
# {
#     'valor': 5,
#     'proximo': None
#     # None
# }

def exibeLista():
    if not lista:
        print('lista vazia.')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']

    print('.')

def adicionarNoFim( elemento):
    global lista
    if not lista:
        lista = {'valor':elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor':elemento, 'proximo': None}

exibeLista()
print('adicionando o 5')
adicionarNoFim(5)
exibeLista()
print('adicionando o 8')
adicionarNoFim(8)
exibeLista()
print('adicionando o 13')
adicionarNoFim(13)
exibeLista()