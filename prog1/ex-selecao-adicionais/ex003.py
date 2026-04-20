# Corrigido

trabalho = float(input('Digite a nota do trabalho: '))
semestral = float(input('Digite a nota da avaliação semestral: '))
exameFinal = float(input('Digite a nota do exame final: '))

media = ((trabalho * 2) + (semestral * 3) + (exameFinal * 5)) / 10

if media >= 8 and media <= 10:
    conceito = 'A'
elif media >= 7 and media < 8:
    conceito = 'B'
elif media >= 6 and media < 7:
    conceito = 'C'
elif media >= 5 and media < 6:
    conceito = 'D'
elif media >= 0 and media < 5:
    conceito = 'E'
else:
    conceito = 'Valor inválido'

print(f'Média ponderada: {media}')
print(f'Conceito: {conceito}')