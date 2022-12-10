from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

class graph(Frame):
    def __init__(self, master:Tk,controller:object) -> None:
        super().__init__(master,bg="#292929")

        # ---Titulo do frame---
        Label(self,text="Escolha os eixos:",bg="#292929",fg="white", font='Ivi 13 bold').grid(row=0,column=0,columnspan=2)

        # ---Label para o eixo X---
        Label(self,text="Eixo X",bg="#292929",fg="white", font='Ivi 10 bold').grid(row=1,column=0)

        # ---Label para o eixo Y---
        Label(self,text="Eixo Y",bg="#292929",fg="white", font='Ivi 10 bold').grid(row=2,column=0)

        # ---Entry para o eixo x---
        self.x_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.x_axis.grid(row=1,column=1)

        # ---Entry para o eixo y---
        self.y_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.y_axis.grid(row=2,column=1)

        # ---Botao para plotar o grafico---
        Button(self,text="Plotar",width=17,bg="black",fg="white",command=lambda : self.plotar(controller)).grid(row=4,column=0,columnspan=2)

        # ---Botao para voltar ao menu---
        Button(self,text="Voltar",width=17,bg="black",fg="white",command= lambda: controller.switchWindows(1,0)).grid(row=5,column=0,columnspan=2)

        self.pack(padx = 0, pady = 0,fill="both",expand=True)
    

    def plotar(self,controller:object) ->None:
        """Funcao que plota um grafico apos escolhidos seus eixos"""
        
        # Tratando as excecoes
        if self.x_axis.get() == "" or self.y_axis.get() == "":

            messagebox.showerror(message="Selecione os eixos")
        else:

            dicionario = {"comprimento sepala":0,"largura sepala":1,"comprimento petala":2,"largura petala":3}

            eixo_x = dicionario[self.x_axis.get()]
            eixo_y = dicionario[self.y_axis.get()]

            plt.xlabel(self.x_axis.get())
            plt.ylabel(self.y_axis.get())

            #Tratando as excecoes
            if self.x_axis.get() == self.y_axis.get():
                if not (messagebox.askyesno(message="Eixos iguais, deseja continuar?")):
                    return 0 #Return early para acabar com a funcao

            #Plotando a as setosas
            plt.plot(controller.banco_dados.setosa[eixo_x],controller.banco_dados.setosa[eixo_y],"or",label="setosa")
            
            #Plotando as versicolors
            plt.plot(controller.banco_dados.versicolor[eixo_x],controller.banco_dados.versicolor[eixo_y],"xb",label="versicolor")

            #Plotando as virginicas
            plt.plot(controller.banco_dados.virginica[eixo_x],controller.banco_dados.virginica[eixo_y],"*g",label="virginica")

            plt.legend() #Adicionando a legenda
            plt.show() #Exibindo o resultado
    
