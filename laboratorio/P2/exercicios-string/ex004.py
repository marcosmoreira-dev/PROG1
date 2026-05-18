# Peça ao usuário para digitar uma frase. Seu programa deve contar e exibir quantas palavras existem nessa frase

frase = input('Digite uma frase: ')
fraseLista = frase.split(' ')
tam = len(fraseLista)

print(f'A quantidade de palavras nessa frase é igual a {tam}')