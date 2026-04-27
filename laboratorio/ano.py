dia = int(input(''))
mes = int(input(''))
ano = int(input(''))

if ano >= 0:
    if mes >= 1 and mes <= 12:
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            diaMax = 31
        elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            diaMax = 30
        else:
            if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
                diaMax = 29
            else:
                diaMax = 28
        if dia >= 1 and dia <= diaMax:
            print('Data válida')
        else:
            print('Data inválida')
    else:
        print('Data inválida')
else:
    print('Data inválida')