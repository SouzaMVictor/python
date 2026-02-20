nomes = [
    'joao',
    'antonio',
    'pedro',
    'bernardo',
    'matheus',
    'bruno'
]

tabela = {}

for nome in nomes:
    qtd = len(nome)
    # qtd = nome[0]
    # {'j': ['joao'], 'a': ['antonio'], 'p': ['pedro'], 'b': ['bernardo', 'bruno'], 'm': ['matheus']}
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)