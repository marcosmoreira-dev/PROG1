
# Dúvidas
# Como limpar a tela?

# Cria a matriz que representa o tabuleiro
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Cria uma função que cria um cabecalho
def cabecalho():
    print(' Bem Vindo ao Jogo da Velha ')
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

vencedor = False
jogadas = 0
vez = 'X'

cabecalho()

# Laço aninhado para percorrer a matriz (linhas e colunas)
# O laço externo pega cada linha
organizaJogo()

# Cria um laço While para permanecer efetuando enquanto não existe um vencedor e o número de jogadas é menor ou igual a 9.
while vencedor != True and jogadas <= 9:
    print(f'É a vez do jogador: {vez}')

    # Pede o input para saber em qual linha e coluna o jogador deseja efetuar a jogada
    linha = int(input('Insira a linha em que deseja jogar: '))
    coluna = int(input('Insira a coluna em que deseja jogar: '))

    if velha[linha][coluna] == ' ':
        # Insere o valor definido no lugar correto
        # Caso seja a vez do jogador X
        if vez == 'X':
            velha[linha][coluna] = 'X'
            jogadas += 1
            vez = 'O'
        # Caso seja a vez do jogador O
        elif vez == 'O':
            velha[linha][coluna] = 'O'
            vez = 'X'
            jogadas += 1
        limpaTela()
        cabecalho()
        organizaJogo()
        
    # CONSERTAR ESSA PARTE DO IF E ELSE PARA SABER QUANDO JÁ ESTÁ OCUPADO A POSIÇÃO
    elif velha[linha][coluna] == 'X' or velha[linha][coluna] == 'O':
        cabecalho()
        organizaJogo() 
        print('A jogada é inválida')
        print('Jogue novamente')
    