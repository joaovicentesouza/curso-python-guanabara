numero = int(input('Digite um número de 1 a 10: '))
tabuada = list(range(1,11))

for i in tabuada:
    print('{} X {} é igual a '.format(numero, i), (numero * i))