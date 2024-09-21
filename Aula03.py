#Author: Eloisa Souza
#Data:Setembro 2024
#Codigos Iniciais em Python

valor = eval(input('Entre com um número positivo'))

potencia = 1
contador = 0

while valor >= potencia:
    potencia = potencia*2
    contador = contador+1

print(f'A maior potencia de 2 menor que {valor} é 2 elevado a {contador - 1}, que vale {potencia/2}')
