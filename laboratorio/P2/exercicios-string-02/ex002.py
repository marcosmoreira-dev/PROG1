# Crie uma ferramenta para criptografar e descriptografar mensagens usando a Cifra de César, uma técnica de substituição simples em que cada letra de um texto pe "deslocada" um certo número de posições no alfabeto.
# Etapas: 
# Crie três variáveis
# Mensagem: a string a ser criptografada
# Chave: um número inteiro que define o deslocamento
# Modo: uma string que pode ser "criptografar" ou "descriptografar"
# Ignore espaços e pontuações, mantendo-os como estão
# Funcionar apenas para letras do alfabeto (sem acentos)
# Garantir que o alfabeto seja circular (depois de 'z' vem 'a')
# Se o modo for "descriptografar", o processo deve ser inverso

mensagem = input('Digite a mensagem: ').upper()
chave = int(input('Digite a chave: '))
modo = input('Digite o modo (c = criptografar / d = descriptografar): ').lower()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nova_frase = ''

# Se o modo for descriptografar,
# a chave precisa andar para trás no alfabeto
if modo == 'd':
    chave = -chave

# Percorre cada caractere da mensagem
for caractere in mensagem:

    # Verifica se o caractere está no alfabeto
    if caractere in alfabeto:

        # Encontra a posição atual da letra
        indice_atual = alfabeto.index(caractere)

        # Calcula a nova posição com deslocamento circular
        novo_indice = (indice_atual + chave) % 26

        # Adiciona a nova letra na frase final
        nova_frase += alfabeto[novo_indice]

    else:
        # Mantém espaços e pontuações sem alteração
        nova_frase += caractere

# Exibe o resultado
if modo == 'c':
    print(f'Mensagem criptografada: {nova_frase}')

elif modo == 'd':
    print(f'Mensagem descriptografada: {nova_frase}')

else:
    print('Modo inválido!')