from heapq import *
fila_prioridade = []

heappush(fila_prioridade, (2, 'atender cliente VIP'))
heappush(fila_prioridade, (1, 'situação critica'))
heappush(fila_prioridade, (3, 'respodner email'))
heappush(fila_prioridade, (1, 'apagar incendio'))

while fila_prioridade:
    prioridade, tarefa = heappop(fila_prioridade)
    print(f'executando a tarefa: {tarefa} - prioridade: {prioridade}')