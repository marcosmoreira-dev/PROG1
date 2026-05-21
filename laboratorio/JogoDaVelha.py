
# Dúvidas
# Como limpar a tela?
# Onde verificar empate?

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

def verificaVencedor(vez):
    # Verifica linhas de X
    if (velha[0][0] == 'X' and velha[0][1] == 'X' and velha[0][2] == 'X' 
        or velha[1][0] == 'X' and velha[1][1] == 'X' and velha[1][2] == 'X' 
        or velha[2][0] == 'X' and velha[2][1] == 'X' and velha[2][2] == 'X'):
        print('O Jogador X venceu!')
        return True
    
    
    # Verifica linhas de 0
    elif (
        velha[0][0] == 'O' and velha[0][1] == 'O' and velha[0][2] == 'O' 
        or velha[1][0] == 'O' and velha[1][1] == 'O' and velha[1][2] == 'O' 
        or velha[2][0] == 'O' and velha[2][1] == 'O' and velha[2][2] == 'O'
        ):
        print('O Jogador O venceu!')
        return True
    
    # Verifica colunas de X
    elif (
        velha[0][0] == 'X' and velha[1][0] == 'X' and velha[2][0] == 'X' 
        or velha[0][1] == 'X' and velha[1][1] == 'X' and velha[2][1] == 'X' 
        or velha[0][2] == 'X' and velha[1][2] == 'X' and velha[2][2] == 'X'
        ):
       print('O Jogador X venceu!')
       return True
    
    # Verifica colunas de O
    elif (
        velha[0][0] == 'O' and velha[1][0] == 'O' and velha[2][0] == 'O' 
        or velha[0][1] == 'O' and velha[1][1] == 'O' and velha[2][1] == 'O' 
        or velha[0][2] == 'O' and velha[1][2] == 'O' and velha[2][2] == 'O'
        ):
       print('O Jogador O venceu!')
       return True
    
    # Verifica diagonais para X
    elif (
        velha[0][0] == 'X' and velha[1][1] == 'X' and velha[2][2] == 'X'
        or velha[0][2] == 'X' and velha[1][1] == 'X' and velha [2][0] == 'X'
        ):
       print('O Jogador X venceu!')
       return True
    
    # Verifica diagonais para O
    elif (
        velha[0][0] == 'O' and velha[1][1] == 'O' and velha[2][2] == 'O'
        or velha[0][2] == 'O' and velha[1][1] == 'O' and velha [2][0] == 'O'
        ):
       
       print('O Jogador O venceu!')
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
print() #EMPATE    