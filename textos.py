# frase = ' O curso de Lógica de Programação é supimpa! '
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

# def analisadorDeTextos(texto):
#     palavras = texto.split()
#     num_palavras = len(palavras)
#     num_caracteres = len(texto)
#     num_caracteres_sem_espacos = num_caracteres - texto.count(' ')
#     return num_palavras, num_caracteres, num_caracteres_sem_espacos

# num_p, num_c, num_cse = analisadorDeTextos(frase)

# print(f'numero palabras: {num_p}')
# print(f'numero caracteres: {num_c}')
# print(f'numero caracs sem espaco: {num_cse}')

# tarefa - montar um contador de palavras repetidas numa frase

# frase2 = 'A tecnologia moderna exige disciplina, e disciplina constante, porque sem disciplina nenhuma evolução acontece, e evolução verdadeira depende de foco, foco diário, foco intenso e foco absoluto naquilo que realmente importa, importa de verdade e importa profundamente.'

# def contadorDePalavrasRepetidas(texto):
#     palavras = texto.split()
#     print(f'palavras: {palavras}')
#     contagem = {}
#     for palavra in palavras:
#         palavra = palavra.strip('.,')
#         if palavra in contagem:
#             # contagem[palavra] += 1
#             contagem[palavra] = contagem[palavra] + 1
#         else:
#             contagem[palavra] = 1
#     print(f'contagem: {contagem}')

# contadorDePalavrasRepetidas(frase2)

# tarefa - montar um contador de frases (separado por ponto final)

frase3 = 'A disciplina constrói resultados sólidos e resultados duradouros. O foco constante gera progresso constante e progresso real. A prática diária fortalece a mente e fortalece a habilidade. O esforço contínuo produz crescimento contínuo e crescimento visível. A repetição consciente melhora o desempenho e melhora a confiança. A organização clara evita erros desnecessários e evita retrabalho constante. A atenção aos detalhes transforma trabalho comum em trabalho excelente. A persistência silenciosa supera talento distraído e supera desculpas frágeis. A consistência diária vence motivação passageira e vence entusiasmo temporário. A evolução verdadeira exige paciência verdadeira e exige compromisso firme.'

# def contadorDeFrases(texto):
#     frases = texto.split('.')
#     print(f'frases: {frases}')
#     print()
#     frases_limpa = [f.strip() for f in frases]
#     print(f'frases limpa: {frases_limpa}')
#     print()
#     frases_validas = [f for f in frases_limpa if len(f) > 0]
#     print(f'frases validas: {frases_validas}')
#     print()
#     print(f'quantidade de frases: {len(frases_validas)}')

# contadorDeFrases(frase3)

# refatorar e melhorar

def separadorDeFrases(texto):
    frases = texto.split('.')
    return [f.strip() for f in frases if f.strip()]

def contadorDeFrases(texto):
    return len(separadorDeFrases(texto))

print(f'quantidade de frases: {contadorDeFrases(frase3)}')