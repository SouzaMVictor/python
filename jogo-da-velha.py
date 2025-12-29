tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
# array de linhas e colunas do tabuleiro.
# cada array dentro da array principal representa uma linha do tabuleiro

jogador = "X"

def exibeTabuleiro():
    for linha in tabuleiro: 
        # exibe cada linha do tabuleiro, linha foi definida no for(podia ser qualquer nome)
        print ("|".join(linha))
        print("-" * 6)

def jogada(linha, coluna):
    # atribui o valor do jogador na posição escolhida
    # na array tabuleiro, eu pego a linha (que é a primeira array) e a coluna (que é o elemento dentro da array), conforme os parâmetros da função
    if not 0 <= linha <= 2 or not 0 <= coluna <= 2 or tabuleiro[linha][coluna] != " ":
        #qualquer coisa que nao for isso vai dar erro
        print("jogada inválida")
        return jogador
    tabuleiro [linha][coluna] = jogador
#volto pro mesmo jogador
    return "O" if jogador == "X" else "X"
 #retorno O se o jogador for X, senao for O, é X

def temGanhador():
    #verifica linhas
    for linha in range (3):
        if(
            tabuleiro [linha][0] != " " and
            tabuleiro [linha][0] == tabuleiro[linha][1] and
            tabuleiro [linha][0] == tabuleiro[linha][2] 
        ):
            print(f'{tabuleiro[linha][0] } é o vencedor!')
            return True
   
    #verifica colunas
    for coluna in range (3):
        if (
            tabuleiro [0][coluna] != " " and
            tabuleiro [0][coluna] == tabuleiro[1][coluna] and
            tabuleiro [0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} é o vencedor!')
            return True

    #verifica diagonais
        if(
            tabuleiro[1][1] != " " and
            (tabuleiro[0][0] == tabuleiro[1][1] and
            tabuleiro[0][0] == tabuleiro[2][2]) or
            (tabuleiro [0][2] == tabuleiro[1][1] and
            tabuleiro [1][1] == tabuleiro[2][0])
        ):
            print(f'{tabuleiro[1][1]} é o vencedor!')
            return True
    #se nao teve nenhum vencedor
    return False
while True:
    print (f'jogador da vez: {jogador}')
    try:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        jogador = jogada (linha, coluna)
    except (ValueError):
        print("Entrada invalida. Digite valores numéricos entre 0 e 2.")
    except (IndexError):
        print("Entrada invalida. Os valores devem ser números inteiros.")
    exibeTabuleiro()
    if temGanhador():
        break