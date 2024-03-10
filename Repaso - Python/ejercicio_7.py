def EsStep(numero):
    numero_str = str(numero)

    for i in range(len(numero_str) - 1):
        diferencia = abs(int(numero_str[i]) - int(numero_str[i + 1]))
    if diferencia == 1:
        print('el numero es step')
    else:
        print('el numero NO es step')
        

numero = int(input('ingrese un numero para verificar si es step: '))
EsStep(numero)