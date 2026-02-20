# nomes = [
#     'joao',
#     'antonio',
#     'pedro',
#     'bernardo',
#     'matheus',
#     'bruno'
# ]
texto = 'Tem gente que diz que carro é só meio de transporte. Eu discordo frontalmente. Carro de verdade é experiência sensorial, é conversa entre máquina e motorista. Um Escort XR3 1988, por exemplo, não te mima com direção elétrica nem te protege com camadas de assistências invisíveis. Ele exige presença. Cada curva é uma negociação, cada troca de marcha é uma decisão consciente. Você não dirige distraído, você dirige envolvido.\
\
Os carros antigos têm algo que a indústria moderna parece ter esquecido: personalidade. Hoje tudo é tela, modo de condução e isolamento acústico exagerado. Antes, o barulho do motor fazia parte da trilha sonora, o volante transmitia as imperfeições do asfalto, e o pedal respondia sem filtro. Era mecânico, direto, quase bruto. E é justamente aí que mora o charme. Não é confortável? Às vezes não. Mas é autêntico.\
\
E quando a gente fala de cupês clássicos, aí o negócio sobe de nível. Um Karmann Ghia 1969 cupê não é apenas um carro; é escultura sobre rodas. Linha baixa, proporções elegantes, aquele perfil que parece desenhado com régua e ousadia. Pintado em um verde profundo e sofisticado, então, vira declaração de identidade. Não é sobre ir do ponto A ao ponto B, é sobre como você chega lá.\
\
Existe também o fator cultural. Carros antigos, especialmente os produzidos no Brasil nas décadas passadas, carregam história industrial, memória afetiva e uma estética que não foi pensada por algoritmo. Eles nasceram numa época em que o design precisava impressionar sem depender de LED, multimídia ou pacote tecnológico. Era lata, vidro, borracha e visão criativa. E isso tem um valor que planilha nenhuma consegue medir.\
\
No fim das contas, gostar de carro antigo é quase um posicionamento filosófico. É escolher sentir mais e automatizar menos. É aceitar que a direção pode ser pesada, que não tem ar-condicionado gelando igual freezer, mas que cada quilômetro percorrido deixa uma lembrança real. Pode não ser a escolha mais prática, mas definitivamente é a mais viva.'

palavras = texto.split()
tabela = {}

for palavra in palavras:
   index = palavra[0].upper()
   if index not in tabela:
    tabela[index] = []
   tabela[index].append(palavra)

for chave, valor in tabela.items():
  print(f'{chave}: {valor}')

