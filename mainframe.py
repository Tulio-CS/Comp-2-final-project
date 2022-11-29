from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import csv
from math import sqrt

 
class menu(Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        Button(self,text="Mostrar estatisticas",width=15).pack(fill="both",expand=True)
        Button(self,text="Mostrar graficos",width=15,command= lambda: controller.switchWindows(0,1)).pack(fill="both",expand=True)
        Button(self,text="Classificar amostra",width=15,command= lambda: controller.switchWindows(0,2)).pack(fill="both",expand=True)
        Button(self,text="sair",width=15,command= lambda: self.sair()).pack(fill="both",expand=True)
        self.pack(padx = 1, pady = 1,fill="both",expand=True)

    def sair(self):
        root.destroy()

class Analisar(Frame):
    def __init__(self,master,controller):
        super().__init__(master)
        Label(self,text="Insira os dados").grid(row=0,column=0,columnspan=2)
        Label(self,text="Comprimento da sepala:",width=20).grid(row=1,column=0)
        self.com_sep = Entry(self,width=15).grid(row=1,column=1)
        Label(self,text="Largura da sepala:",width=20).grid(row=2,column=0)
        self.lar_sep = Entry(self,width=15).grid(row=2,column=1)
        Label(self,text="Comprimento da petala:",width=20).grid(row=3,column=0)
        self.com_pet = Entry(self,width=15).grid(row=3,column=1)
        Label(self,text="Comprimento da petala:",width=20).grid(row=4,column=0)
        self.lar_pet = Entry(self,width=15).grid(row=4,column=1)
        Button(self,text="Voltar",width=15,command= lambda: controller.switchWindows(2,0)).grid(row=5,column=0)
        self.pack()
        Button(self,text="Analisar",width=15,command= lambda: controller.switchWindows(2,0)).grid(row=5,column=1)
    
    def analisar(self,controller):
        min_dist = int
        classificacao = str
        with open("C:/Users/tulio/OneDrive/Documentos/GitHub/Comp-2-final-project/iris.csv") as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    for i in range(1,len(data)):
                        if data[i][4] == "setosa":
                            for j in range(4):
                                controller.banco_dados[0][j].append(data[i][j])
                        if data[i][4] == "versicolor":
                            for j in range(4):
                                controller.banco_dados[1][j].append(data[i][j])
                        if data[i][4] == "virginica":
                            for j in range(4):
                                controller.banco_dados[2][j].append(data[i][j])

    def distancia_euclidiana_4D(self,x,y,z,w):
        """Eixo x = comprimento sepala
           Eixo y = largira sepala
           Eixo z = comprimento petala
           Eixo w = largura petala"""
        dist = (((self.com_sep - x) ** 2) + ((self.lar_sep - y) ** 2) + ((self.com_pet - z) ** 2) + ((self.lar_pet - w) ** 2))
        return dist

        
        
 
class graph(Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        Label(self,text="Escolha os eixos").grid(row=0,column=0,columnspan=2)
        Label(self,text="Eixo X").grid(row=1,column=0)
        Label(self,text="Eixo Y").grid(row=2,column=0)
        self.x_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.x_axis.grid(row=1,column=1)
        self.y_axis = ttk.Combobox(self,width=17,state="readonly",values=["comprimento sepala","largura sepala","comprimento petala","largura petala"])
        self.y_axis.grid(row=2,column=1)
        Button(self,text="Plotar",width=17,command=lambda : self.plotar(controller)).grid(row=3,column=0,columnspan=2)
        Button(self,text="Voltar",width=17,command= lambda: controller.switchWindows(1,0)).grid(row=4,column=0,columnspan=2)
        self.pack()

    def plotar(self,controller):
        dicionario = {"comprimento sepala":0,"largura sepala":1,"comprimento petala":2,"largura petala":3}
        plt.xlabel(self.x_axis.get())
        plt.ylabel(self.y_axis.get())
        plt.plot(controller.banco_dados[0][dicionario[self.x_axis.get()]],controller.banco_dados[0][dicionario[self.y_axis.get()]],"or",label="setosa")
        plt.plot(controller.banco_dados[1][dicionario[self.x_axis.get()]],controller.banco_dados[1][dicionario[self.y_axis.get()]],"xb",label="versicolor")
        plt.plot(controller.banco_dados[2][dicionario[self.x_axis.get()]],controller.banco_dados[2][dicionario[self.y_axis.get()]],"*g",label="virginica")
        plt.legend()
        plt.show()

class Controller:
    def __init__(self,master):
        mainframe = Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=True)
        self.banco_dados = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.windowNum = 0
        self.framelist = []
        page_menu = menu(mainframe,self)
        page_graph = graph(mainframe,self)
        page_analisar = Analisar(mainframe,self)
        self.framelist.append(page_menu)
        self.framelist.append(page_graph)
        self.framelist.append(page_analisar)
        self.framelist[1].forget()
        self.framelist[2].forget()
        self.rotina_csv()

    def rotina_csv(self):
        with open("C:/Users/tulio/OneDrive/Documentos/GitHub/Comp-2-final-project/iris.csv") as f:
            reader = csv.reader(f)
            data = list(reader)
            for i in range(1,len(data)):
                if data[i][4] == "setosa":
                    for j in range(4):
                        self.banco_dados[0][j].append(data[i][j])
                if data[i][4] == "versicolor":
                    for j in range(4):
                        self.banco_dados[1][j].append(data[i][j])
                if data[i][4] == "virginica":
                    for j in range(4):
                        self.banco_dados[2][j].append(data[i][j])

    
     
    def switchWindows(self,atual,proxima):
        self.framelist[atual].forget()
        self.framelist[proxima].tkraise()
        self.framelist[proxima].pack(padx = 10, pady = 10)
        
 
root = Tk()
Controller(root)
root.title("")
root.mainloop()