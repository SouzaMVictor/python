from collections import deque

def criarPilha():
    return deque()

def insereNaPilha(pilha, elemento):
        pilha.append(elemento)

def removeDaPilha(pilha):
    return pilha.pop()

pilha = criarPilha()

print(pilha)

insereNaPilha(pilha, 8)
insereNaPilha(pilha, 9)
insereNaPilha(pilha, 10)
insereNaPilha(pilha, 11)
insereNaPilha(pilha, 12)
print(f'ver pilha atual: {pilha}')
print(f'removendo {removeDaPilha(pilha)}')
print(f'removendo {removeDaPilha(pilha)}')
print(pilha)