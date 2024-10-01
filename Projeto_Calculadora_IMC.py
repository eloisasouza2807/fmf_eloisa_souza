#Author:Eloisa Souza Nascimento
#Data:Setembro 2024
#Projeto 01

peso = int(input('Insira o seu peso:'))
altura = float(input('Insira a sua altura:'))
imc = peso / altura**2
resultado = imc

if resultado < 18.5:
    print('Seu IMC é: Abaixo do peso')
elif 18.5 and resultado < 25:
    print('Seu IMC é: Normal')
elif 25 and resultado < 30:
    print('Seu IMC é: Sobrepeso')
else:
    print('Seu IMC é: Obesidade')
