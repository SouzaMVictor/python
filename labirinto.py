import random

def criar_labirinto(tamanho):
    labirinto = [[ random.randint(0,1) for _ in range (tamanho)] for _ in range (tamanho)]
    labirinto[0][0] = 8
    labirinto[ tamanho - 1 ][ tamanho - 1 ] = 9
    return labirinto

def exibir_labirinto(labirinto):
    for linha in labirinto:
        print(linha)

def nao_pode_seguir(labirinto, linha, coluna):
    if (linha >= len(labirinto) or
        coluna >= len(labirinto) or
        linha < 0 or
        coluna < 0 or
        labirinto [linha][coluna] == 1 or labirinto [linha][coluna] == 2):
        return True

def explorar_labirinto(labirinto, linha, coluna):
    print(f'explorando ({linha},{coluna})')
    if nao_pode_seguir(labirinto, linha, coluna):
        print(f'nao pode seguir ({linha}, {coluna})')
        return False
    
    if labirinto[linha][coluna] == 9:
        print('chegou ao final')
        return True
    
    # marcar posição visitada

    labirinto[linha][coluna] = 2

    return (
        explorar_labirinto(labirinto, linha, coluna + 1) or #direita
        explorar_labirinto(labirinto, linha + 1, coluna) or #baixo
        explorar_labirinto(labirinto, linha, coluna - 1) or #esquerda
        explorar_labirinto(labirinto, linha - 1, coluna) #cima
    )

lab = criar_labirinto(5)
exibir_labirinto(lab)

explorar_labirinto(lab, 0, 0)