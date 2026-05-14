mensagem = input('Digite a mensagem: ')
chave = int(input('Digite a chave: '))
modo = input('Digite o modo: (c/d): ').lower()

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabetoNovo = alfabeto
criptografada = ''

if modo == "c":
    for i in mensagem:
        deslocamento = alfabeto[i+chave]