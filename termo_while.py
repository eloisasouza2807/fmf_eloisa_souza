#Author:Eloisa Souza
#Data:Agosto 2024
#Codigos Iniciais Python

termo = soma = contador = 1
while termo >= 0.01:
    termo *= 0.5
    soma += termo
    contador +=1
    print('A soma dos {contador} termos vale {soma}.')
    print(f'O {contador+1} termo vale {termo} e ficou abaixo de 0.01.')
