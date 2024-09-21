#Author:Eloisa Souza
#Data:Agosto 2024
#Codigos Iniciais Python

fator = 1
contador = 0
taxa = eval(input('Entre com a taxa de juros anual em porcentagens:'))
while fator < 1.5:
    fator+= fator*taxa/100
    contador += 1
    print(f'São necessários {contador} anos para atingir 50% de rentabilidade com a taxa de {taxa} % ao ano')

