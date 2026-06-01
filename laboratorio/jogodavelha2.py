# Cria a matriz que representa o tabuleiro
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Cria uma função que cria um cabecalho
def cabecalho():
    print('---------TABULEIRO ---------')
    print('\n')

# Cria uma função que organiza o jogo
def organizaJogo():
# Laço aninhado para percorrer a matriz (linhas e colunas)
# O laço externo pega cada linha
    for l in range(len(velha)):
        # O laço interno pega cada célula da linha atual
        for c in range(len(velha[l])):
            print(f' {velha[l][c] }', end=" | ")
        # Pula uma linha para a próxima fileira do tabuleiro
        print('\n---------------')

# Cria uma função que "limpa a tela"
def limpaTela():
    # Adiciona 100 linhas
    print('\n' * 100)

def verificaVencedor(vencedor):
    # Verifica linhas de X
    if (velha[0][0] == 'X' and velha[0][1] == 'X' and velha[0][2] == 'X' 
        or velha[1][0] == 'X' and velha[1][1] == 'X' and velha[1][2] == 'X' 
        or velha[2][0] == 'X' and velha[2][1] == 'X' and velha[2][2] == 'X'):
        print('O Jogador X venceu!')
        vencedor = True
        return vencedor
    
    
    # Verifica linhas de 0
    elif (
        velha[0][0] == 'O' and velha[0][1] == 'O' and velha[0][2] == 'O' 
        or velha[1][0] == 'O' and velha[1][1] == 'O' and velha[1][2] == 'O' 
        or velha[2][0] == 'O' and velha[2][1] == 'O' and velha[2][2] == 'O'
        ):
        print('O Jogador O venceu!')
        vencedor = True
        return vencedor
    
    # Verifica colunas de X
    elif (
        velha[0][0] == 'X' and velha[1][0] == 'X' and velha[2][0] == 'X' 
        or velha[0][1] == 'X' and velha[1][1] == 'X' and velha[2][1] == 'X' 
        or velha[0][2] == 'X' and velha[1][2] == 'X' and velha[2][2] == 'X'
        ):
       print('O Jogador X venceu!')
       vencedor = True
       return vencedor
    
    # Verifica colunas de O
    elif (
        velha[0][0] == 'O' and velha[1][0] == 'O' and velha[2][0] == 'O' 
        or velha[0][1] == 'O' and velha[1][1] == 'O' and velha[2][1] == 'O' 
        or velha[0][2] == 'O' and velha[1][2] == 'O' and velha[2][2] == 'O'
        ):
       print('O Jogador O venceu!')
       vencedor = True
       return vencedor
    
    # Verifica diagonais para X
    elif (
        velha[0][0] == 'X' and velha[1][1] == 'X' and velha[2][2] 
        or velha[0][2] == 'X' and velha[1][1] == 'X' and velha [2][0] == 'X'
        ):
       print('O Jogador X venceu!')
       vencedor = True
       return vencedor
    
    # Verifica diagonais para O
    elif (
        velha[0][0] == 'O' and velha[1][1] == 'O' and velha[2][2] 
        or velha[0][2] == 'O' and velha[1][1] == 'O' and velha [2][0] == 'O'
        ):
       
       print('O Jogador O venceu!')
       vencedor = True
       return vencedor
    return False

vencedor = False
jogadas = 0
vez = 'X'

print(' Bem Vindo ao Jogo da Velha ')
cabecalho()

# Laço aninhado para percorrer a matriz (linhas e colunas)
# O laço externo pega cada linha
organizaJogo()
