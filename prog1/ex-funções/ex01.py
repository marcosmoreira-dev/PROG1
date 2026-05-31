# Construa um módulo que identifique se um número é, ou não, primo.

def verificaPrimo(num):
    if num <= 1:
        return False
    
    ePrimo = True
    candidatoDivisor = 2
    while (candidatoDivisor != num and ePrimo):
        if num % candidatoDivisor == 0:
            ePrimo = False
        else:
            candidatoDivisor += 1

    return ePrimo

# OU

def verificaPrimo2(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
