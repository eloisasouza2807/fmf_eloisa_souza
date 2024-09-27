import tkinter
from tkinter.ttk import Button, Label

#Estrutura da janela
Calculadora = tkinter.Tk()
Calculadora.title('Calculadora de IMC')
Calculadora.geometry('475x500+500+100')
Calculadora.resizable(False, False)
Calculadora.configure(bg='#800000')

#função que ativa os botões numéricos
def btNumeros(numero):
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, 'end')
    campoNumeros.insert(0, str(pegaNumero)+str(numero))
    return
def limpaCampo():
    campoNumeros.delete(0, 'end')
    return

def soma():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'soma'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def subtracao():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'subtracao'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def multiplicacao():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'multiplicacao'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def divisao():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'divisao'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def porcentagem():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'porcentagem'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def potencia():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'potencia'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def raiz():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'raiz'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def igual():
    pegaNumero = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'igual'
    primeiroNumero = int(pegaNumero)
    campoNumeros.delete(0, 'end')
    return

def igual():
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, 'end')
    if operacao == 'soma':
        campoNumeros.insert(0, str(primeiroNumero)+pegaNumero)
    elif operacao == 'subtracao':
        campoNumeros.insert(0, str(primeiroNumero)-pegaNumero)
    elif operacao == 'multiplicacao':
        campoNumeros.insert(0, str(primeiroNumero)*int(pegaNumero))
    elif operacao == 'divisao':
        campoNumeros.insert(0,primeiroNumero / int(pegaNumero))
    elif operacao == 'porcentagem':
        campoNumeros.insert(0,(primeiroNumero* int(pegaNumero))/100)
    elif operacao == 'raiz':
        campoNumeros.insert(0, primeiroNumero ** (1/2))
    elif operacao == 'potencia':
        campoNumeros.insert(0, (primeiroNumero) ** int(pegaNumero))
    return





#Entry
campoNumeros = tkinter.Entry(Calculadora, width = 50)
campoNumeros.place(x = 100, y = 25)

#Botões
Bt1 = Button(Calculadora, text='1', width=10, command=lambda : btNumeros(1))
Bt1.place(x=50, y=150)
Bt2 = Button(Calculadora, text='2', width=10, command=lambda : btNumeros(2))
Bt2.place(x=150, y=150)
Bt3 = Button(Calculadora, text='3', width=10, command=lambda : btNumeros(3))
Bt3.place(x=250, y=150)
Bt4 = Button(Calculadora, text='4', width=10, command=lambda : btNumeros(4))
Bt4.place(x=50, y=225)
Bt5 = Button(Calculadora, text='5', width=10, command=lambda : btNumeros(5))
Bt5.place(x=150, y=225)
Bt6 = Button(Calculadora, text='6', width=10, command=lambda : btNumeros(6))
Bt6.place(x=250, y=225)
Bt7 = Button(Calculadora, text='7', width=10, command=lambda : btNumeros(7))
Bt7.place(x=50, y=300)
Bt8 = Button(Calculadora, text='8', width=10, command=lambda : btNumeros(8))
Bt8.place(x=150, y=300)
Bt9 = Button(Calculadora, text='9', width=10, command=lambda : btNumeros(9))
Bt9.place(x=250, y=300)
Bt0 = Button(Calculadora, text='0', width=10, command=lambda : btNumeros(0))
Bt0.place(x=150, y=375)
BtVirgula = Button(Calculadora, text='.', width=10)
BtVirgula.place(x=50, y=375)
BtIgual = Button(Calculadora, text='=', width=10, command=igual)
BtIgual.place(x=250, y=375)
BtDivisao = Button(Calculadora, text='/', width=10, command=divisao)
BtDivisao.place(x=350, y=150)
BtMultiplicacao = Button(Calculadora, text='x', width=10, command=multiplicacao)
BtMultiplicacao.place(x=350, y=225)
BtSoma = Button(Calculadora, text='+', width=10, command=soma)
BtSoma.place(x=350, y=300)
BtSubtracao = Button(Calculadora, text='-', width=10, command=subtracao)
BtSubtracao.place(x=350, y=375)
BtC = Button(Calculadora, text='C', width=10, command=limpaCampo)
BtC.place(x=50, y=75)
BtPorcentagem = Button(Calculadora, text='%', width=10, command=porcentagem)
BtPorcentagem.place(x=150, y=75)
BtPotencia = Button(Calculadora, text='xⁿ', width=10, command=potencia)
BtPotencia.place(x=250, y=75)
BtRaiz = Button(Calculadora, text='√', width=10, command=raiz)
BtRaiz.place(x=350, y=75)

FeitoPor = Label(Calculadora, text='Desenvolvido por Eloisa Souza')
FeitoPor.place(x=150, y=455)
Calculadora.mainloop()