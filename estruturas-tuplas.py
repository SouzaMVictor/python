import subprocess
import os

# gerenciador de tarefas

tarefas = []

def adicionarTarefas(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibirTarefas(tarefa):
    if not tarefas:
        print('a lista esta vazia')
        return
    for tarefa in tarefas:
        print(f'tarefa: {tarefa[0]} - status: {tarefa[1]} ')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [ (t[0], 'concluida') if t[0] == tarefa else t for t in tarefas]

def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]


def buscarTarefa(tarefa):
    # for t in tarefas:
    #     if t[0] == tarefa:
    #         print(f'tarefa encontrada: {t[0]} - status: {t[0]}')
    #         return
    # print(f'nao achei: {tarefa}')

    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower()]
    if resultado :
        for titulo, status in resultado:
            print(f'encontrada : {titulo} -  status: {status}')
    else:
        print(f'tarefa nao encontrada: {tarefa}')

while True:
    os.system('cls')
    print('-----')
    print('boas vindas ao gerenciador de tarefas')
    print('-----')
    print('o que vc quer fazer agora?')
    print('1- listar tarefas')
    print('2- adicionar tarefas')
    print('3- remover tarefas')
    print('4- marcar tarefa como concluida')
    print('5- buscar tarefa')
    print('0- sair do gerenciador')
    opcao =  int(input('digite uma opcao: '))

    match opcao:
        case 1: 
            exibirTarefas(tarefa)
        case 2:
            tarefa = input('digite a tarefa: ')
            adicionarTarefas(tarefa)
        case 3:
            tarefa = input('digite a tarefa: ')
            removerTarefa(tarefa)
        case 4:
            tarefa = input('digite a tarefa: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('digite a tarefa: ')
            buscarTarefa(tarefa)
        case 0:
            break
        case _:
            print('opcao invalida...')
    print()
    input('pressione enter para continuar...')

            