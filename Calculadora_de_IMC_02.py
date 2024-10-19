#Author:Eloisa Souza Nascimento
#Data:Outubro 2024
#Projeto 02

from tkinter import *
from tkinter import messagebox

# Cores e fontes
co0 = '#ffffff'
co1 = '#8B0000'
co2 = '#800000'
font_style = ('Helvetica', 12)

janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('400x300')
janela.configure(background=co0)

# Função para calcular o IMC
def calcular():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())
        imc = peso / altura ** 2
        resultado = '{:.2f}'.format(imc)

        if imc < 18.5:
            resultado_texto = 'Abaixo do peso'
        elif 18.5 <= imc < 25:
            resultado_texto = 'Normal'
        elif 25 <= imc < 30:
            resultado_texto = 'Sobrepeso'
        else:
            resultado_texto = 'Obesidade'

        l_resultado.config(text=resultado_texto)
        l_resultado_texto.config(text=f'O seu IMC é: {resultado}')

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Configuração da interface
frame_cima = Frame(janela, background=co0)
frame_cima.pack(pady=10)

app_nome = Label(frame_cima, text='Calculadora de IMC', font=('Helvetica', 16, 'bold'), bg=co0, fg=co1)
app_nome.pack()

frame_baixo = Frame(janela, background=co0)
frame_baixo.pack(pady=20)

l_peso = Label(frame_baixo, text='Insira seu peso:', font=font_style, bg=co0, fg=co1)
l_peso.grid(row=0, column=0, padx=10, pady=5)

e_peso = Entry(frame_baixo, width=10, relief='solid', font=font_style)
e_peso.grid(row=0, column=1, padx=10, pady=5)

l_altura = Label(frame_baixo, text='Insira sua altura:', font=font_style, bg=co0, fg=co1)
l_altura.grid(row=1, column=0, padx=10, pady=5)

e_altura = Entry(frame_baixo, width=10, relief='solid', font=font_style)
e_altura.grid(row=1, column=1, padx=10, pady=5)

l_resultado = Label(frame_baixo, text='---', font=('Helvetica', 20, 'bold'), bg=co0, fg=co2)
l_resultado.grid(row=2, columnspan=2, pady=20)

l_resultado_texto = Label(frame_baixo, text='O seu IMC é:', font=font_style, bg=co0, fg=co1)
l_resultado_texto.grid(row=3, columnspan=2)

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=15, font=font_style, bg=co2, fg=co0)
b_calcular.grid(row=4, columnspan=2, pady=10)

# Limpar campos
def limpar():
    e_peso.delete(0, END)
    e_altura.delete(0, END)
    l_resultado.config(text='---')
    l_resultado_texto.config(text='O seu IMC é:')

b_limpar = Button(frame_baixo, command=limpar, text='Limpar', width=15, font=font_style, bg=co2, fg=co0)
b_limpar.grid(row=5, columnspan=2, pady=5)

janela.mainloop()
