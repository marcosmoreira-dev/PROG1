senhaCorreta = 'Python'
senha = input('Digite a senha: ')

while senha != senhaCorreta:
    print('Senha incorreta')
    senha = input('Digite a senha novamente: ')
print('Senha correta!')
