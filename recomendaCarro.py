
"""
@author: Joao da Silva Muniz Neto && Mateus Monteiro Santos
"""

import tkinter as tk
from PIL import ImageTk
import regrasRecomendacao as rules
from experta import Fact
import tkinter.font as tkFont

#Busca nas regras qual recomendacao foi redirecionada    
def detectarRecomendacao():    
    sistemaEspecialista = rules.RegrasRecomendacao()
    sistemaEspecialista.reset()
    
    sistemaEspecialista.declare(Fact(tipoHatch = str(escolhaTipoHatch.get())))
    sistemaEspecialista.declare(Fact(tipoSeda = str(escolhaTipoSeda.get())))
    sistemaEspecialista.declare(Fact(tipoSuv = str(escolhaTipoSuv.get())))
    sistemaEspecialista.declare(Fact(motor1t = str(escolhaMotor1t.get())))
    sistemaEspecialista.declare(Fact(motor14t = str(escolhaMotor14t.get())))
    sistemaEspecialista.declare(Fact(motor2t = str(escolhaMotor2t.get())))
    sistemaEspecialista.declare(Fact(manual = str(escolhaManual.get())))
    sistemaEspecialista.declare(Fact(automatico = str(escolhaAutomatico.get())))
    sistemaEspecialista.declare(Fact(ar_condicionado = str(escolhaAr_condicionado.get())))
    sistemaEspecialista.declare(Fact(farol_de_milha = str(escolhaFarol_de_milha.get())))
    sistemaEspecialista.declare(Fact(camera_de_re = str(escolhaCamera_de_re.get()))) 
    sistemaEspecialista.declare(Fact(direcao_eletrica = str(escolhaDirecao_eletrica.get()))) 
    sistemaEspecialista.declare(Fact(vidros_eletricos = str(escolhaVidros_eletricos.get()))) 
    sistemaEspecialista.declare(Fact(piloto_automatico = str(escolhaPiloto_automatico.get()))) 

    sistemaEspecialista.run()
    
    carroRecomendado.config(state = tk.NORMAL)
    coresDisponiveis.config(state = tk.NORMAL)
    precoCarro.config(state = tk.NORMAL)
    
    carroRecomendado.delete("1.0", "end")
    carroRecomendado.insert(tk.INSERT, sistemaEspecialista.carro)
    coresDisponiveis.delete("1.0", "end")
    coresDisponiveis.insert(tk.INSERT, sistemaEspecialista.cordoCarro)
    precoCarro.delete("1.0", "end")
    precoCarro.insert(tk.INSERT, sistemaEspecialista.precodoCarro)
    
    carroRecomendado.config(state = tk.DISABLED)
    coresDisponiveis.config(state = tk.DISABLED)
    precoCarro.config(state = tk.DISABLED)

#Limpando os campos utilizados
def limpiar():
    carroRecomendado.config(state = tk.NORMAL)
    coresDisponiveis.config(state = tk.NORMAL)
    precoCarro.config(state = tk.NORMAL)
    
    carroRecomendado.delete("1.0", "end")
    coresDisponiveis.delete("1.0", "end")
    precoCarro.delete("1.0", "end")
    
    carroRecomendado.config(state = tk.DISABLED)
    coresDisponiveis.config(state = tk.DISABLED)
    precoCarro.config(state = tk.DISABLED)
    
    escolhaTipoHatch.set(False)
    escolhaTipoSeda.set(False)
    escolhaTipoSuv.set(False)
    escolhaMotor1t.set(False)
    escolhaMotor14t.set(False)
    escolhaMotor2t.set(False)
    escolhaManual.set(False)
    escolhaAutomatico.set(False)
    escolhaAr_condicionado.set(False)
    escolhaFarol_de_milha.set(False)
    escolhaCamera_de_re.set(False)
    escolhaDirecao_eletrica.set(False)
    escolhaVidros_eletricos.set(False)
    escolhaPiloto_automatico.set(False)
    
background = "#99f6ff"
raiz = tk.Tk()
raiz.title("PyCar - recomendando carros a rodo")
raiz.geometry("+350+20")
raiz.config(bg= background)

#variaveis de escolha dos campos selecionados
escolhaTipoHatch = tk.BooleanVar()    
escolhaTipoSeda = tk.BooleanVar()    
escolhaTipoSuv = tk.BooleanVar() 
escolhaMotor1t = tk.BooleanVar() 
escolhaMotor14t = tk.BooleanVar() 
escolhaMotor2t = tk.BooleanVar() 
escolhaManual = tk.BooleanVar() 
escolhaAutomatico = tk.BooleanVar() 
escolhaAr_condicionado = tk.BooleanVar() 
escolhaFarol_de_milha = tk.BooleanVar() 
escolhaCamera_de_re = tk.BooleanVar() 
escolhaDirecao_eletrica = tk.BooleanVar() 
escolhaVidros_eletricos = tk.BooleanVar() 
escolhaPiloto_automatico = tk.BooleanVar()  

#interface do programa (iniciando com o titulo)
fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
l1 = tk.Label(raiz, text="Marque as opções que você deseja", width=30, bg=background,  font=fontStyle)
l1.grid(row = 0, column = 1, pady = 5, padx=5 )

#Titulo tipo do carro
fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Tipo do carro", width=60, bg=background, font=fontTipo).grid(row = 1, column = 1, pady = 5)

#caixa de selecao do tipo Hatch
img1 = ImageTk.PhotoImage(file = "./fotos/hatch.jpg")
c1 = tk.Checkbutton(raiz, text = "Hatch", variable = escolhaTipoHatch, image = img1,  width=100, height=100, compound='top', bg= background)
c1.grid(row = 2, column = 0, pady = 5)

#caixa de selecao do tipo Sedan
img2 = ImageTk.PhotoImage(file = "./fotos/sedan.jpg")
c2 = tk.Checkbutton(raiz, text = "Sedan", variable = escolhaTipoSeda, image = img2,  width=100, height=100, compound='top', bg=background)
c2.grid(row = 2, column = 1, pady = 5)

#caixa de selecao do tipo SUV
img3 = ImageTk.PhotoImage(file = "./fotos/suv.jpg")
c3 = tk.Checkbutton(raiz, text = "SUV", variable = escolhaTipoSuv, image = img3,  width=100, height=100, compound='top', bg=background)
c3.grid(row = 2, column = 2, pady = 5)

#Titulo motor do carro
tk.Label(raiz, text="Motor do carro", width=60, bg=background, font=fontTipo).grid(row = 3, column = 1, pady = 5)

#caixa de selecao do Motor 1.0 Turbo
img4 = ImageTk.PhotoImage(file = "./fotos/motor1t.jpg")
c4 = tk.Checkbutton(raiz, text = "Motor 1.0 turbo", variable = escolhaMotor1t, image = img4,  width=100, height=100, compound='top', bg=background)
c4.grid(row = 4, column = 0, pady = 5)

#caixa de selecao do Motor 1.4 turbo
img5 = ImageTk.PhotoImage(file = "./fotos/motor1.4t.jpg")
c5= tk.Checkbutton(raiz, text = "Motor 1.4 turbo", variable = escolhaMotor14t, image = img5,  width=100, height=100, compound='top', bg=background)
c5.grid(row = 4, column = 1, pady = 5)

#caixa de selecao do Motor 2.0 turbo
img6 = ImageTk.PhotoImage(file = "./fotos/motor2t.jpg")
c6 = tk.Checkbutton(raiz, text = "Motor 2.0 turbo", variable = escolhaMotor2t, image = img6,  width=100, height=100, compound='top', bg=background)
c6.grid(row = 4, column = 2, pady = 5) 

#Titulo cambio do carro
tk.Label(raiz, text="Cambio do carro", width=60, bg=background, font=fontTipo).grid(row = 5, column = 1, pady = 5)

#caixa de selecao do cambio manual
img7 = ImageTk.PhotoImage(file = "./fotos/cambio-manual.jpg")
c7 = tk.Checkbutton(raiz, text = "Manual", variable = escolhaManual, image = img7,  width=100, height=100, compound='top', bg=background)
c7.grid(row = 6, column = 0, padx= 10, pady = 10)

#caixa de selecao do cambio automatico
img8 = ImageTk.PhotoImage(file = "./fotos/cambio-automatico.jpg")
c8 = tk.Checkbutton(raiz, text = "Automatico", variable = escolhaAutomatico, image = img8,  width=100, height=110, compound='top',bg=background)
c8.grid(row = 6, column = 1, padx=10, pady = 10)

#Titulo opcionais do carro
tk.Label(raiz, text="Opcionais do carro", width=60, bg=background, font=fontTipo).grid(row = 7, column = 1, pady = 5)

#caixa de selecao do Ar condicionado
img9 = ImageTk.PhotoImage(file = "./fotos/ar_condicionado.jpg")
c9 = tk.Checkbutton(raiz, text = "Ar condicionado", variable = escolhaAr_condicionado, image = img9,  width=100, height=100, compound='top', bg=background)
c9.grid(row = 8, column = 2, pady = 5)

#caixa de selecao do Farol de milha
img10 = ImageTk.PhotoImage(file = "./fotos/farol_de_milha.jpg")
c10 = tk.Checkbutton(raiz, text = "Farol de milha", variable = escolhaFarol_de_milha, image = img10,  width=100, height=110, compound='top', bg=background)
c10.grid(row = 8, column = 0, pady = 5)

#caixa de selecao do Camera de re
img11 = ImageTk.PhotoImage(file = "./fotos/camera-re.jpg")
c11 = tk.Checkbutton(raiz, text = "Camera de re", variable = escolhaCamera_de_re, image = img11,  width=100, height=100, compound='top', bg=background)
c11.grid(row = 8, column = 1, pady = 5)

#caixa de selecao do Direcao eletrica
img12 = ImageTk.PhotoImage(file = "./fotos/direcao_eletrica.jpg")
c12 = tk.Checkbutton(raiz, text = "Direcao eletrica", variable = escolhaDirecao_eletrica, image = img12,  width=100, height=100, compound='top', bg=background)
c12.grid(row = 9, column = 2, pady = 5)

#caixa de selecao do Vidros eletricos
img13 = ImageTk.PhotoImage(file = "./fotos/vidro_eletrico.jpg")
c13 = tk.Checkbutton(raiz, text = "Vidros eletricos", variable = escolhaVidros_eletricos, image = img13,  width=100, height=100, compound='top', bg=background)
c13.grid(row = 9, column = 0, pady = 5)

#caixa de selecao do Piloto automatico
img14 = ImageTk.PhotoImage(file = "./fotos/piloto_automatico.jpg")
c14 = tk.Checkbutton(raiz, text = "Piloto automatico", variable = escolhaPiloto_automatico, image = img14,  width=100, height=100, compound='top', bg=background)
c14.grid(row = 9, column = 1, pady = 5)

#caixa Confirmar
b1 = tk.Button(raiz, text="Confirmar", command = detectarRecomendacao, bg=background)
b1.grid(row = 10, column = 0, padx = 10, pady=10)

#caixa Limpar areas selecionadas
b2 = tk.Button(raiz, text="Limpar areas selecionadas", command = limpiar, bg=background)
b2.grid(row = 10, column = 2, padx = 5, pady=10 )

####    layout tela final: modelo do carro, disponibilidade de cores e preço final    ####

#resposta de qual carro foi recomendado
l2 = tk.Label(raiz, text = "Esse é seu carro:", bg=background)
l2.grid(row = 11, column = 0, pady = 2)
carroRecomendado = tk.Text(raiz, state = tk.DISABLED, height = 1, width=40)
carroRecomendado.grid(row = 11, column = 1, pady = 2)

#resposta de qual cor tem disponibilizada
l3 = tk.Label(raiz, text="Cores disponiveis:", bg=background)
l3.grid(row = 12, column = 0, pady = 2)
coresDisponiveis = tk.Text(raiz, state = tk.DISABLED, height = 1, width=40)
coresDisponiveis.grid(row = 12, column = 1, pady = 2)

#resposta do preço do carro
l4 = tk.Label(raiz, text="Preço do carro:", bg=background)
l4.grid(row = 13, column = 0, pady = 2)
precoCarro = tk.Text(raiz, state = tk.DISABLED, height = 1, width=40)
precoCarro.grid(row = 13, column = 1, pady = 2)

#loop da main para funcionamento do aplicativo
raiz.mainloop()