# Cria a matriz que representa o tabuleiro
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

vencedor = False
jogadas = 0
vez = 'X'

print(' Bem Vindo ao Jogo da Velha ')
print(' ---- TABULEIRO ----')

# Laço aninhado para percorrer a matriz (linhas e colunas)
# O laço externo pega cada linha
for l in range(len(velha)):
    # O laço interno pega cada célula da linha atual
    for c in range(len(velha[l])):
        print(f' {velha[l][c] }', end=" | ")
    # Pula uma linha para a próxima fileira do tabuleiro
    print('\n---------------')

# Cria um laço While para permanecer efetuando enquanto não existe um vencedor e o número de jogadas é menor ou igual a 9.
while vencedor != True and jogadas <= 9:
    print(f'É a vez do jogador: {vez}')

    # Pede o input para saber em qual linha e coluna o jogador deseja efetuar a jogada
    linha = int(input('Insira a linha em que seja jogar: '))
    coluna = int(input('Insira a coluna em que deseja jogar: '))

    # Insere o valor definido no lugar correto
    if vez == 'X':
        velha[linha][coluna] = 'X'
        print(velha)
    elif vez == 'O':
        velha[linha][coluna] = 'O'
        print(velha)
    