from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

class graph(Frame):
    def __init__(self, master,controller):
        super().__init__(master,bg="#292929")
        Label(self,text="Escolha os eixos",bg="#292929",fg="white").grid(row=0,column=0,columnspan=2)
        Label(self,text="Eixo X",bg="#292929",fg="white").grid(row=1,column=0)
        Label(self,text="Eixo Y",bg="#292929",fg="white").grid(row=2,column=0)
        self.x_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.x_axis.grid(row=1,column=1)
        self.y_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.y_axis.grid(row=2,column=1)
        Button(self,text="Plotar",width=17,bg="#292929",fg="white",command=lambda : self.plotar(controller)).grid(row=3,column=0,columnspan=2)
        Button(self,text="Voltar",width=17,bg="#292929",fg="white",command= lambda: controller.switchWindows(1,0)).grid(row=4,column=0,columnspan=2)
        self.pack()

    def plotar(self,controller):
        dicionario = {"comprimento sepala":0,"largura sepala":1,"comprimento petala":2,"largura petala":3}
        eixo_x = dicionario[self.x_axis.get()]
        eixo_y = dicionario[self.y_axis.get()]
        plt.xlabel(self.x_axis.get())
        plt.ylabel(self.y_axis.get())
        plt.plot(controller.banco_dados.setosa[eixo_x],controller.banco_dados.setosa[eixo_y],"or",label="setosa")
        plt.plot(controller.banco_dados.versicolor[eixo_x],controller.banco_dados.versicolor[eixo_y],"xb",label="versicolor")
        plt.plot(controller.banco_dados.virginica[eixo_x],controller.banco_dados.virginica[eixo_y],"*g",label="virginica")
        plt.legend()
        plt.show()