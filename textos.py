frase = ' O curso de Lógica de Programação é supimpa! '
# print(f'primeira letra: {frase[0]}')
# print(f'ultima letra: {frase[-1]}')
# print(f'tamanho da frase: {len(frase)}')
# print(f'maiuscualas: {frase.upper()}')
# print(f'minusculas: {frase.lower()}')
# print()
# print(f'fatiando: {frase.split('a')}')
# print(f'fatiando: {frase.split()}')
# print(f'limpando: {frase.strip()}')
# print(f'tamanho da string limpa:{len(frase.strip())}')

def analisadorDeTextos(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    num_caracteres_sem_espacos = num_caracteres - texto.count(' ')
    return num_palavras, num_caracteres, num_caracteres_sem_espacos

num_p, num_c, num_cse = analisadorDeTextos(frase)

print(f'numero palabras: {num_p}')
print(f'numero caracteres: {num_c}')
print(f'numero caracs sem espaco: {num_cse}')

# tarefa - montar um contador de palavras repetidas numa frase

