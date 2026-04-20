# Não corrigido

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print('Média = ', media)

if media >= 0 and media < 3:
    print('Aluno reprovado')
elif media >= 3 and media < 7:
    print('Exame')
elif media >= 7 and media <= 10:
    print('Aprovado')
else:
    print('A nota da média não está entre 0 e 10.')