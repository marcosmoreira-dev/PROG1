# Escreva um programa que leia 5 pares de 2 valores, o primeiro representando a matrícula de um aluno e o segundo representando a sua altura em centímetros. Encontrar o aluno mais alto e o mais baixo e escrever suas matrículas, suas alturas e uma mensagem dizendo se é o mais alto ou o mais baixo.

matricula = int(input('Digite a matrícula do aluno: '))
altura = float(input('Digite a altura do respectivo aluno: '))
maisAlto = altura
matriculaMaisAlto = matricula
maisBaixo = altura
matriculaMaisBaixo = matricula


for i in range (4):
    matricula = int(input('Digite a matrícula do aluno: '))
    altura = float(input('Digite a altura do respectivo aluno: '))

    if altura > maisAlto:
        maisAlto = altura
        matriculaMaisAlto = matricula
    elif altura < maisBaixo:
        maisBaixo = altura
        matriculaMaisBaixo = matricula

print(f'Mais alto = {maisAlto} e tem matrícula {matriculaMaisAlto}')
print(f'Mais baixo = {maisBaixo} e tem matrícula {matriculaMaisBaixo}')