#Author:Eloisa Souza Nascimento
#Data:Setembro 2024
#Projeto 01

#Peso do usuário
peso = int(input('Insira o seu peso:'))
#Altura
altura = float(input('Insira a sua altura:'))
#Calcular IMC
imc = peso / altura**2
#Imprimir o IMC
resultado = imc

if resultado < 18.5:
    print('Seu IMC é: Abaixo do e_peso')
elif 18.5 and resultado < 25:
    print('Seu IMC é: Normal')
elif 25 and resultado < 30:
    print('Seu IMC é: Sobrepeso')
else:
    print('Seu IMC é: Obesidade')
