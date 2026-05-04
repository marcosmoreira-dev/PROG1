for i in range(55):
    a = int(input('Digite o primeiro lado do triângulo: '))
    b = int(input('Digite o primeiro lado do triângulo: '))
    c = int(input('Digite o primeiro lado do triângulo: '))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1/2)