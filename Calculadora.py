#Author:Eloisa Souza Nascimento
#Data:Setembro 2024
#Projeto de calculadora aritmética

import tkinter
from tkinter.ttk import Button, Label

# Estrutura da janela
Calculadora = tkinter.Tk()
Calculadora.title('Calculadora de IMC')
Calculadora.geometry('475x500+500+100')
Calculadora.resizable(False, False)
Calculadora.configure(bg='#800000')

# Função que ativa os botões numéricos
def btNumeros(numero):
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, 'end')
    campoNumeros.insert(0, str(pegaNumero) + str(numero))

def limpaCampo():
    campoNumeros.delete(0, 'end')

def setOperacao(op):
    global primeiroNumero, operacao
    pegaNumero = campoNumeros.get()
    primeiroNumero = float(pegaNumero) if pegaNumero else 0
    operacao = op
    campoNumeros.delete(0, 'end')

def igual():
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, 'end')
    try:
        segundoNumero = float(pegaNumero) if pegaNumero else 0
        if operacao == 'soma':
            campoNumeros.insert(0, primeiroNumero + segundoNumero)
        elif operacao == 'subtracao':
            campoNumeros.insert(0, primeiroNumero - segundoNumero)
        elif operacao == 'multiplicacao':
            campoNumeros.insert(0, primeiroNumero * segundoNumero)
        elif operacao == 'divisao':
            if segundoNumero == 0:
                campoNumeros.insert(0, "Erro")
            else:
                campoNumeros.insert(0, primeiroNumero / segundoNumero)
        elif operacao == 'porcentagem':
            campoNumeros.insert(0, (primeiroNumero * segundoNumero) / 100)
        elif operacao == 'raiz':
            campoNumeros.insert(0, primeiroNumero ** 0.5)
        elif operacao == 'potencia':
            campoNumeros.insert(0, primeiroNumero ** segundoNumero)
    except ValueError:
        campoNumeros.insert(0, "Erro")

# Entry
campoNumeros = tkinter.Entry(Calculadora, width=50)
campoNumeros.place(x=100, y=25)

# Botões
for i in range(10):
    Button(Calculadora, text=str(i), width=10, command=lambda num=i: btNumeros(num)).place(x=(50 + (i % 3) * 100), y=(150 + (i // 3) * 75))

BtVirgula = Button(Calculadora, text='.', width=10, command=lambda: btNumeros('.'))
BtVirgula.place(x=50, y=375)

BtIgual = Button(Calculadora, text='=', width=10, command=igual)
BtIgual.place(x=250, y=375)
BtDivisao = Button(Calculadora, text='/', width=10, command=lambda: setOperacao('divisao'))
BtDivisao.place(x=350, y=150)
BtMultiplicacao = Button(Calculadora, text='x', width=10, command=lambda: setOperacao('multiplicacao'))
BtMultiplicacao.place(x=350, y=225)
BtSoma = Button(Calculadora, text='+', width=10, command=lambda: setOperacao('soma'))
BtSoma.place(x=350, y=300)
BtSubtracao = Button(Calculadora, text='-', width=10, command=lambda: setOperacao('subtracao'))
BtSubtracao.place(x=350, y=375)
BtC = Button(Calculadora, text='C', width=10, command=limpaCampo)
BtC.place(x=50, y=75)
BtPorcentagem = Button(Calculadora, text='%', width=10, command=lambda: setOperacao('porcentagem'))
BtPorcentagem.place(x=150, y=75)
BtPotencia = Button(Calculadora, text='xⁿ', width=10, command=lambda: setOperacao('potencia'))
BtPotencia.place(x=250, y=75)
BtRaiz = Button(Calculadora, text='√', width=10, command=lambda: setOperacao('raiz'))
BtRaiz.place(x=350, y=75)

FeitoPor = Label(Calculadora, text='Desenvolvido por Eloisa Souza')
FeitoPor.place(x=150, y=455)
Calculadora.mainloop()
