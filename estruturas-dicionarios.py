estudantes = {
    1: { 'nome': 'victor', 'idade': 26, 'curso': 'computação' },
    2: { 'nome': 'ana', 'idade': 22, 'curso': 'engenharia civil' },
    3: { 'nome': 'carlos', 'idade': 30, 'curso': 'direito' },
    4: { 'nome': 'mariana', 'idade': 19, 'curso': 'design gráfico' },
    5: { 'nome': 'joão', 'idade': 28, 'curso': 'administração' },
    6: { 'nome': 'beatriz', 'idade': 24, 'curso': 'psicologia' },
    7: { 'nome': 'rafael', 'idade': 27, 'curso': 'computação' },  # repetido
    8: { 'nome': 'larissa', 'idade': 21, 'curso': 'arquitetura' },
    9: { 'nome': 'felipe', 'idade': 23, 'curso': 'computação' },  # repetido
    10: { 'nome': 'juliana', 'idade': 29, 'curso': 'medicina' },
    11: { 'nome': 'bruno', 'idade': 25, 'curso': 'medicina' },  # repetido
    12: { 'nome': 'camila', 'idade': 20, 'curso': 'engenharia civil' }  # repetido
}

cursos = {
 'computação',
 'engenharia civil',
 'direito',
 'design gráfico',
 'administração',
 'psicologia',
 'sistemas de informação',
 'arquitetura',
 'ciência de dados',
 'medicina'
}

estudantesCursos = {
    'computação': {1, 7, 9},
    'engenharia civil': {2, 12},
    'direito': {3},
    'design gráfico': {4},
    'administração': {5},
    'psicologia': {6},
    'sistemas de informação': {7},
    'arquitetura': {8},
    'ciência de dados': {9},
    'medicina': {10, 11}
}

def adicionarEstudante(matricula, nome, idade, curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa
    if curso not in estudantesCursos:
        estudantesCursos[curso] = set()
    estudantesCursos[curso].add(matricula)


adicionarEstudante(13, 'pedrinho', 19, 'medicina')
print (f'todas as pessoas matriculadas em algum curso: {estudantesCursos["medicina"] | estudantesCursos["computação"]}')