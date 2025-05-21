import tkinter as tk

# CORES PRINCIPAIS- (Se quiser mudar fica a vontade)
preto = '#000000'
branco = "#F5F5F5"
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

#Divisão das janelas - inferior

janela_inferior = tk.Frame(janela,
width=300,
height=50,
relief='flat',
bg=preto)

janela_inferior.grid(row=1,column=0,sticky='NSEW')

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