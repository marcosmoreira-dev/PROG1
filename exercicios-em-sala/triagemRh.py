# Um departamento de RH precisa de um script para automatizar a triagem de candidatos para uma vaga de Analista de Informática. O programa deve receber a nota da prova técnica (0 a 100), os anos de experiência do candidato e se ele possui graduação na área ("S" ou "N"). A pontuação final do candidato é calculada da seguinte forma: a prova técnica tem peso 6 e a experiencia tem peso 4 (considere que cada ano de experiência vale 10 pontos, até o limite de 100 pontos para o cálculo)
# Aprovado para Entrevista: Pontuação final maior ou igual a 80 e possui graduação
# Banco de Talentos: Pontuação final maior ou igual a 70 (independente de graduação) ou tem mais de 5 anos de experiência
# Desclassificado: Qualquer outra situação. Calcule a pontuação final e exiba a situação do candidato.

nota = float(input('Digite a nota da prova técnica: '))
experiencia = int(input('Digite os anos de experiência na área: '))
graduacao = input('Você possui graduação na área (S/N): ').upper()

if experiencia <= 10:
    pontosExperiencia = experiencia * 10
else:
    pontosExperiencia = 100

pontuacaoFinal = ((nota * 6) + (pontosExperiencia * 4)) / 10


if pontuacaoFinal >= 80 and graduacao == 'S':
    situcao = 'Aprovado para Entrevista'
elif pontuacaoFinal >= 70 or experiencia > 5:
    situcao = 'Banco de Talentos'
else:
    situcao = 'Desclassificado'

print(f'Pontuação final: {situcao}')
print(f'Pontuação final: {pontuacaoFinal}')