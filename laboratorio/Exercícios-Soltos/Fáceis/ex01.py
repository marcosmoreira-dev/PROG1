# Crie uma tupla contendo os dias da semana.
# Peça ao usuário um número de 1 a 7 e exiba o dia correspondente.
# Exemplo: 
# Digite um número: 3
# Quarta-feira

dias_semana = ("Segunda-feira", 
               "Terça-Feira", 
               "Quarta-feira", 
               "Quinta-feira", 
               "Sexta-feira", 
               "Sábado", 
               "Domingo")

n = int(input('Digite um número: '))
print(dias_semana[n - 1])