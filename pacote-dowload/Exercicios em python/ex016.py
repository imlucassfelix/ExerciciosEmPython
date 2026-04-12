#utilizi função para imprimir parte inteira de um numero 
#utilizei função para imprimir parte inteira de um número 
import math
valor=float(input('Digite um valor:'))
parte=math.trunc(valor)
print('O número {} tem a parte inteira {}'.format(valor,parte))