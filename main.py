lista_numeros = [1, 6, 13]

for numero in lista_numeros:
    if numero == 1:
        pass

    elif (numero % 2) == 0:
        for item in range(2, numero+1, 2):
            print(item)
        print('-' * 10)
    else:
        for item in range(2, numero, 2):
            print(item)

