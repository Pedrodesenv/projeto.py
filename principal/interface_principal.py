import tkinter as tk

# CORES PRINCIPAIS- (Se quiser mudar fica a vontade)
preto = 'black'
branco = "white"
verde = "#32CD32"

# CORES DE IMC - tipo uma tabela com a classificação

'''
amarela = 
verde = peso normal

'''

#Criando a Janela

janela = tk.Tk()
janela.title('Calculadora de IMC')
janela.geometry('350x200')
janela.config(bg=preto)


#Divisão das janelas - superior

janela_superior = tk.Frame(janela,width=300,height=50,relief='flat',bg=preto)
janela_superior.grid(row=0,column=0,sticky='NSEW')

label_janela = tk.Label(janela_superior,
text='Calculadora de IMC',
padx=5,
pady=5,
bg=preto,
fg=verde,
font=('Sans Serif',16,'bold'))

label_janela.pack()

# Linha decorativa
app_linha = tk.Label(
    janela_superior,
    text="",
    width=350,
    height=1,
    anchor="center",
    padx=0,
    pady=0,
    relief="flat",
    font=("ivy 1"),
    bg=verde,
    fg=verde
)
app_linha.pack()


janela_inferior = tk.Frame(janela,
width=300,
height=50,
relief='flat',
bg=preto)

janela_inferior.grid(row=1,column=0,sticky='NSEW')

text_peso = tk.Label(janela_inferior, text="insira seu peso", height=1, padx=0, anchor='center', relief="flat", font=("ivy 10 bold "), bg=preto, fg=verde)
text_peso.grid(row=0, column=0, sticky='NSEW', pady=10, padx=3)

caixa_peso = tk.Entry(janela_inferior, width=5, relief="solid", font=("ivy 10 bold "), justify='center')
caixa_peso.grid(row=0, column=1, sticky='NSEW', pady=10, padx=3)

text_altura = tk.Label(janela_inferior, text="insira seu peso", height=1, padx=0, anchor='center', relief="flat", font=("ivy 10 bold "), bg=preto, fg=verde)
text_altura.grid(row=1, column=0, sticky='NSEW', pady=10, padx=3)

caixa_altura = tk.Entry(janela_inferior, width=5, relief="solid", font=("ivy 10 bold "), justify='center')
caixa_altura.grid(row=1, column=1, sticky='NSEW', pady=10, padx=3)

caixa_resultado = tk.Label(janela_inferior, width=5, height=1, padx=6, pady=12, relief="flat", anchor="center", font=("ivy 25 bold "), bg=verde, fg=verde)
caixa_resultado.place(x=170, y=10)

l_resultado_texto = tk.Label(janela_inferior, text="seu resultado é: obesidade", width=37, height=1, padx=10, pady=1, relief="flat", anchor="center", font=("ivy 8 bold "), bg=verde, fg=verde)
l_resultado_texto.place(x=0, y=85)

#Criação da função

def calculo():
    peso = float() # Depois tu usa o entrada_peso.get() que serve como um input
    altura = float()
    imc = peso / altura ** 2
    imc_formatado = f'{imc:.2f}' #apenas duas casas decimais
    
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc > 18.5 and imc < 24.9:
        print('Peso normal')
    elif imc > 25 and imc < 29.9:
        print('Sobrepeso')
    elif imc > 30 and imc < 34.9:
        print('Obesidade grau I')
    elif imc > 35 and imc < 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')


#Deixando a janela sempre aberta
janela.mainloop()