# 1) Crie uma função chamada potencia que receba dois números: a base e o expoente.
# ● Regra: Não é permitido usar o operador de potência nem a função pow(). Deve implementar o cálculo utilizando um laço.
# ● Desafio: Garanta que a função funcione se o expoente for 0 (resultado deve ser 1).

def potencia(base, potencia):
    res = 1
    for i in range(potencia):
        res *= base
    return res

print(potencia(6, 3))