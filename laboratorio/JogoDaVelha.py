import os

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
    os.system('cls')

def verificaVencedor(vez):
    # Verifica linhas
    if (velha[0][0] == vez and velha[0][1] == vez and velha[0][2] == vez 
        or velha[1][0] == vez and velha[1][1] == vez and velha[1][2] == vez 
        or velha[2][0] == vez  and velha[2][1] ==vez  and velha[2][2] == vez):
        print(f'O Jogador {vez} venceu!')
        return True
    
    
    
    # Verifica colunas
    elif (
        velha[0][0] == vez and velha[1][0] == vez and velha[2][0] == vez 
        or velha[0][1] == vez and velha[1][1] == vez and velha[2][1] == vez 
        or velha[0][2] == vez and velha[1][2] == vez and velha[2][2] == vez
        ):
       print(f'O Jogador {vez} venceu!')
       return True
    
    
    # Verifica diagonais
    elif (
        velha[0][0] == vez and velha[1][1] == vez and velha[2][2] == vez
        or velha[0][2] == vez and velha[1][1] == vez and velha [2][0] == vez
        ):
       print(f'O Jogador {vez} venceu!')
       return True
    
    
    return False

vencedor = False
jogadas = 0
vez = 'X'

print(' Bem Vindo ao Jogo da Velha ')
cabecalho()

# Laço aninhado para percorrer a matriz (linhas e colunas)
# O laço externo pega cada linha
organizaJogo()

# Cria um laço While para permanecer efetuando enquanto não existe um vencedor e o número de jogadas é menor ou igual a 9.
while vencedor == False and jogadas < 9:
    print(f'É a vez do jogador: {vez}')

    # Pede o input para saber em qual linha e coluna o jogador deseja efetuar a jogada
    linha = int(input('Insira a linha em que deseja jogar: '))
    coluna = int(input('Insira a coluna em que deseja jogar: '))

    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
        if velha[linha][coluna] == ' ':
            # Insere o valor definido no lugar correto
            # Caso seja a vez do jogador X
            if vez == 'X':
                velha[linha][coluna] = 'X'
                jogadas += 1
                limpaTela()
                cabecalho()
                if verificaVencedor() == True:
                    vencedor = True
                vez = 'O'
                organizaJogo()

            # Caso seja a vez do jogador O
            elif vez == 'O':
                velha[linha][coluna] = 'O'
                jogadas += 1
                limpaTela()
                cabecalho()
                if verificaVencedor() == True:
                        vencedor = True
                vez = 'X'
                organizaJogo()
            
            
        elif velha[linha][coluna] != ' ':
            limpaTela()
            cabecalho()
            organizaJogo() 
            print('A jogada é inválida')
            print('Jogue novamente')
    else: 
        print('A jogada é inválida')
        print('Jogue novamente')      
print('Deu velha!')
print('Obrigado por jogar!')