from collections import deque
def criarFila():
    return deque()


def insereNaFila(fila, elemento):
        fila.append(elemento)

def removeDaFila(fila):
    return fila.popleft()

fila = criarFila()

print(fila)

insereNaFila(fila, 8)
insereNaFila(fila, 9)
insereNaFila(fila, 10)
insereNaFila(fila, 11)
insereNaFila(fila, 12)
print(f'removendo {removeDaFila(fila)}')
print(f'removendo {removeDaFila(fila)}')
print(fila)