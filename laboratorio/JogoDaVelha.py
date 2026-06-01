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
    print(f"\n" * 100)

def verificaVencedor(vez):
    # Verifica se existe vencedor nas linhas
    # Usei o parâmetro/variável "vez" para não precisar repetir o código duas vezes
    if (velha[0][0] == vez and velha[0][1] == vez and velha[0][2] == vez 
        or velha[1][0] == vez and velha[1][1] == vez and velha[1][2] == vez 
        or velha[2][0] == vez  and velha[2][1] ==vez  and velha[2][2] == vez):
        return True
    
    
    
    # Verifica se existe vencedor nas colunas
    elif (
        velha[0][0] == vez and velha[1][0] == vez and velha[2][0] == vez 
        or velha[0][1] == vez and velha[1][1] == vez and velha[2][1] == vez 
        or velha[0][2] == vez and velha[1][2] == vez and velha[2][2] == vez
        ):
       return True
    
    
    # Verifica se existe vencedor nas diagonais
    elif (
        velha[0][0] == vez and velha[1][1] == vez and velha[2][2] == vez
        or velha[0][2] == vez and velha[1][1] == vez and velha [2][0] == vez
        ):
       return True
    
    # Caso não exista vencedor em nenhuma ocasião, retorna False (ou seja, indica que não existe vencedor)
    return False

# Cria uma função para verificar o empate passando o parâmetro do número de jogadas
def verificaEmpate(jogadas):
    # Se chegar no limite de jogadas, o jogo está empatado
    if jogadas == 9:
        return True # Retorna verdadeiro caso o número de jogadas for igual a 9
    else:
        return False # Caso não seja verdadeiro, retorna falso


vencedor = False # Cria uma variável vencedor e inicializa ela com o valor booleano False
jogadas = 0 # Cria uma variável para a contagem de jogadas e inicializa ela como zero
vez = 'X' # Cria a variável "vez" e inicializa ela como sendo X, eu poderia ter pedido o input para o usuário, mas para isso seria necessário verificar a entrada para X ou Y

print(' Bem Vindo ao Jogo da Velha ')
cabecalho()
# Mostra tabuleiro do jogo organizado antes de começar
organizaJogo()

# Cria um laço While para permanecer efetuando enquanto não existe um vencedor e o número de jogadas é menor ou igual a 9.
while vencedor == False and jogadas < 9:
    # Print para indicar a vez do jogador usando a variável "vez"
    print(f'É a vez do jogador: {vez}')

    # Pede o input para saber em qual linha e coluna o jogador deseja efetuar a jogada
    linha = int(input('Insira a linha em que deseja jogar: '))
    coluna = int(input('Insira a coluna em que deseja jogar: '))

    # Cria um If para verificar se as linhas e colunas estão entre 0 e 2
    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
        # If para verificar se o local selecionado está vazio
        if velha[linha][coluna] == ' ':
            # Insere o símbolo do jogador da vez (seja X ou O)
            velha[linha][coluna] = vez
            jogadas += 1

            limpaTela() # Etapa de organização do jogo
            cabecalho()

            # Utiliza a função para verificar se existe vencedor usando a variável vez
            if verificaVencedor(vez): # Se existir vencedor entra no laço
                organizaJogo() 
                print(f'O jogador {vez} venceu!')
                vencedor = True # Determina que tem um vencedor e encerra o laço while
            elif verificaEmpate(jogadas): # Utiliza a função para verificar se existe empates utilizando a variável jogadas
                organizaJogo()
                print('Deu velha!')
                print('Obrigado por jogar')
                vencedor = True # Encerra o jogo em caso de empate
            else:
                # Cria uma operação ternária para não precisar repetir duas vezes o código, uma vez para X e uma para 0
                # Eu pesquisei e foi a melhor maneira que encontrei para não criar um código gigante
                # Se for a vez de X, a varíavel se torna "O", se não (ou seja, se for O) ela se torna X
                vez = 'O' if vez == 'X' else 'X'
                organizaJogo()

        # Caso o local selecionado esteja ocupado entra nesse laço
        elif velha[linha][coluna] != ' ':
            limpaTela()
            cabecalho()
            organizaJogo() 
            print('A jogada é inválida')
            print('Jogue novamente')
    # Caso as variáveis linhas e colunas não estiverem entre 0 e 2, o jogo entra nesse laço
    else: 
        print('A jogada é inválida')
        print('Jogue novamente')