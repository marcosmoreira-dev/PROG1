# Faça um programa que leia a idade de uma pessoa e escreva se a pessoa é 'maior de idade', 'menor de idade' ou 'maior de 65 anos'.

idade = int(input('Digite a sua idade: '))

if idade > 65:
    print('Você é maior de 65 anos.')
elif idade >= 18 and idade <= 65:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')