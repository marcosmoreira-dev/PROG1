# Peça ao usuário um número inteiro N. Escreva um programa que gere e imprima os N primeiros termos da sequência de Fibonacci. A sequência começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores (Ex.: 0, 1, 1, 2, 3, 5, 8, ...)

# Solicita ao usuário um número inteiro N
N = int(input("Digite a quantidade de termos: "))

# Inicializa os dois primeiros termos da sequência
a = 0
b = 1

# Verifica se N é válido
if N <= 0:
    print("Por favor, digite um número positivo.")
else:
    # Gera os N termos da sequência
    for i in range(N):
        print(a)  # imprime o termo atual
        
        # Atualiza os valores:
        # o próximo termo será a soma dos dois anteriores
        # Calcula o próximo termo da sequência (soma dos dois anteriores)
        proximo = a + b
        
        # Atualiza 'a' para o valor atual de 'b'
        # (anda uma posição na sequência)
        a = b
        
        # Atualiza 'b' para o próximo termo calculado
        # (prepara o próximo passo da sequência)
        b = proximo