from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import csv
from math import sqrt
import numpy as np

path = "C:/Users/tulio/OneDrive/Documentos/GitHub/Comp-2-final-project/iris.csv"

class banco_de_dados:
    def __init__(self):
        self.path = path
        self.setosa = np.array([[],[],[],[]])
        self.versicolor = np.array([[],[],[],[]])
        self.virginica = np.array([[],[],[],[]])
            
    def rotina_csv(self):
        setosa = [[],[],[],[]]
        versicolor = [[],[],[],[]]
        virginica = [[],[],[],[]]
        with open(self.path) as f:
            reader = csv.reader(f)
            data = list(reader)
            for i in range(1,len(data)):
                if data[i][4] == "setosa":
                    for j in range(4):
                        setosa[j].append(float(data[i][j]))
                if data[i][4] == "versicolor":
                    for j in range(4):
                        versicolor[j].append(float(data[i][j]))
                if data[i][4] == "virginica":
                    for j in range(4):
                        virginica[j].append(float(data[i][j]))
        self.setosa = np.array(setosa)
        self.virginica = np.array(virginica)
        self.versicolor = np.array(versicolor)
        return 0


 
class menu(Frame):
    def __init__(self, master,controller):
        super().__init__(master,bg="#292929")
        Button(self,text="Mostrar estatisticas",width=15,bg="#3F3F3F",fg="white",command=lambda: controller.switchWindows(0,3)).pack(fill="both",expand=True)
        Button(self,text="Mostrar graficos",width=15,bg="#3F3F3F",fg="white",command= lambda: controller.switchWindows(0,1)).pack(fill="both",expand=True)
        Button(self,text="Classificar amostra",width=15,bg="#3F3F3F",fg="white",command= lambda: controller.switchWindows(0,2)).pack(fill="both",expand=True)
        Button(self,text="sair",width=15,bg="#3F3F3F",fg="white",command= lambda: self.sair(master)).pack(fill="both",expand=True)
        self.pack(padx = 1, pady = 1,fill="both",expand=True)

    def sair(self,master):
        master.master.destroy()

class Analisar(Frame):
    def __init__(self,master,controller):
        super().__init__(master,bg="#292929")
        Label(self,text="Insira os dados",bg="#292929",fg="white").grid(row=0,column=0,columnspan=2)
        Label(self,text="Comprimento da sepala:",width=20,bg="#292929",fg="white").grid(row=1,column=0)
        self.com_sep = Entry(self,width=15,bg="#3F3F3F",fg="white")
        self.com_sep.grid(row=1,column=1)
        Label(self,text="Largura da sepala:",width=20,bg="#292929",fg="white").grid(row=2,column=0)
        self.lar_sep = Entry(self,width=15,bg="#3F3F3F",fg="white")
        self.lar_sep.grid(row=2,column=1)
        Label(self,text="Comprimento da petala:",width=20,bg="#292929",fg="white").grid(row=3,column=0)
        self.com_pet = Entry(self,width=15,bg="#3F3F3F",fg="white")
        self.com_pet.grid(row=3,column=1)
        Label(self,text="Comprimento da petala:",width=20,bg="#292929",fg="white").grid(row=4,column=0)
        self.lar_pet = Entry(self,width=15,bg="#3F3F3F",fg="white")
        self.lar_pet.grid(row=4,column=1)
        Button(self,text="Voltar",width=15,bg="#3F3F3F",fg="white",command= lambda: controller.switchWindows(2,0)).grid(row=5,column=0)
        self.pack()
        Button(self,text="Analisar",width=15,bg="#3F3F3F",fg="white",command= lambda: self.analisar(controller)).grid(row=5,column=1)
    
    def analisar(self,controller):
        min_dist = self.distancia_euclidiana_4D(max(controller.banco_dados.virginica[0]),max(controller.banco_dados.virginica[1]),max(controller.banco_dados.virginica[2]),max(controller.banco_dados.virginica[3]))
        classificacao = "Sem classificação"
        for i in range(len(controller.banco_dados.setosa[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.setosa[0][i],controller.banco_dados.setosa[1][i],controller.banco_dados.setosa[2][i],controller.banco_dados.setosa[3][i])
            if dist <= min_dist:
                min_dist = dist
                classificacao = "setosa"
        for i in range(len(controller.banco_dados.versicolor[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.versicolor[0][i],controller.banco_dados.versicolor[1][i],controller.banco_dados.versicolor[2][i],controller.banco_dados.versicolor[3][i])
            if dist <= min_dist:
                min_dist = dist
                classificacao = "versicolor"
        for i in range(len(controller.banco_dados.virginica[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.virginica[0][i],controller.banco_dados.virginica[1][i],controller.banco_dados.virginica[2][i],controller.banco_dados.virginica[3][i])
            if dist <= min_dist:
                min_dist = dist
                classificacao = "virginica"
        print(classificacao)
        

    def distancia_euclidiana_4D(self,x,y,z,w):
        """Eixo x = comprimento sepala
           Eixo y = largira sepala
           Eixo z = comprimento petala
           Eixo w = largura petala"""
        dist = sqrt(((float(self.com_sep.get()) - x) ** 2) + ((float(self.lar_sep.get()) - y) ** 2) + ((float(self.com_pet.get()) - z) ** 2) + ((float(self.lar_pet.get()) - w) ** 2))
        return dist

        
        
 
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

class Controller:
    def __init__(self,master):
        self.master = master
        master.configure(bg="#292929")
        mainframe = Frame(master,bg="#292929")
        mainframe.pack(padx=10, pady=10, fill='both', expand=True)
        self.banco_dados = banco_de_dados()
        self.banco_dados.rotina_csv()
        self.banco_dados.path = path
        self.windowNum = 0
        self.framelist = []
        page_menu = menu(mainframe,self)
        page_graph = graph(mainframe,self)
        page_analisar = Analisar(mainframe,self)
        page_estatisticas = Estatisticas(mainframe,self)
        self.framelist.append(page_menu)
        self.framelist.append(page_graph)
        self.framelist.append(page_analisar)
        self.framelist.append(page_estatisticas)
        self.framelist[1].forget()
        self.framelist[2].forget()
        self.framelist[3].forget()






    
     
    def switchWindows(self,atual,proxima):
        self.framelist[atual].forget()
        self.framelist[proxima].tkraise()
        self.framelist[proxima].pack(padx = 10, pady = 10)


class Estatisticas(Frame):
    def __init__(self,master,controller):
        super().__init__(master,bg="#292929")
        comprimento_sepala = np.concatenate((controller.banco_dados.setosa[0],controller.banco_dados.versicolor[0],controller.banco_dados.virginica[0]))
        largura_sepala = np.concatenate((controller.banco_dados.setosa[1],controller.banco_dados.versicolor[1],controller.banco_dados.virginica[1]))
        comprimento_petala = np.concatenate((controller.banco_dados.setosa[2],controller.banco_dados.versicolor[2],controller.banco_dados.virginica[2]))
        largura_petala = np.concatenate((controller.banco_dados.setosa[3],controller.banco_dados.versicolor[3],controller.banco_dados.virginica[3]))
        o = 'white'
        a = '#292929'
        print(comprimento_sepala)

        Label(self, text= 'Resumo base de dados iris: 150 elementos', height=1, font='Ivi 15 bold',bg=a, fg=o).grid(row=0)
        Label(self, text= 'comprimento_sepala:', height=1, font='Ivi 13 bold',bg=a, fg=o).grid(row=1,sticky=W)
        Label(self, text= 'Minimo:  '+ str(min(comprimento_sepala)), height=1, padx = 30,font='Ivi 10 bold',bg=a, fg=o ).grid(row=2,sticky=W)
        Label(self, text= 'Maximo:  '+ str(max(comprimento_sepala)), height=1,  padx = 30, font='Ivi 10 bold',bg=a, fg=o ).grid(row=3,sticky=W)
        Label(self, text= 'Media:  '+ str(np.median(comprimento_sepala)), height=1,  padx = 30, font='Ivi 10 bold',bg=a, fg=o ).grid(row=4,sticky=W)
        Label(self, text= 'Desvio padrão::  '+ str(np.std(comprimento_sepala)),  height=1,  padx = 30, font='Ivi 10 bold',bg=a, fg=o ).grid(row=5,sticky=W)


        Label(self, text= 'largura_sépala:', height=1, font='Ivi 13 bold',bg=a, fg=o ).grid(row=6,sticky=W)
        Label(self, text= 'Minimo:  '+ str(min(largura_sepala)), padx = 30, height=1, font='Ivi 10 bold',bg=a, fg=o ).grid(row=7,sticky=W)
        Label(self, text= 'Maximo:  '+ str(max(largura_sepala)), padx = 30, height=1, font='Ivi 10 bold',bg=a, fg=o ).grid(row=8,sticky=W)
        Label(self, text= 'Media:  '+ str(np.median(largura_sepala)),  padx = 30, height=1, font='Ivi 10 bold',bg=a, fg=o ).grid(row=9,sticky=W)
        Label(self, text= 'Desvio padrão::  '+ str(np.std(largura_sepala)),  padx = 30, height=1, font='Ivi 10 bold',bg=a, fg=o ).grid(row=10,sticky=W)


        Label(self, text= 'comprimento_pélata:', height=1,anchor='sw',  font='Ivi 13 bold',bg=a, fg=o ).grid(row=11,sticky=W)
        Label(self, text= 'Minimo:  '+ str(min(comprimento_petala)), padx = 30, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=12,sticky=W)
        Label(self, text= 'Maximo:  '+ str(max(comprimento_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=13,sticky=W)
        Label(self, text= 'Media:  '+ str(np.median(comprimento_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=14,sticky=W)
        Label(self, text= 'Desvio padrão::  '+ str(np.std(comprimento_petala)), width = 45, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=15,sticky=W)


        Label(self, text= 'largura_pélata:', height=1, anchor='sw', font='Ivi 13 bold',bg=a, fg=o ).grid(row=16,sticky=W)
        Label(self, text= 'Minimo:  '+ str(min(largura_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=17,sticky=W)
        Label(self, text= 'Maximo:  '+ str(max(largura_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=18,sticky=W)
        Label(self, text= 'Media:  '+ str(np.median(largura_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=19,sticky=W)
        Label(self, text= 'Desvio padrão:  '+ str(np.std(largura_petala)), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=20 ,sticky=W)


        Label(self,text= 'tipo:', height=1, anchor='sw', font='Ivi 13 bold',bg=a, fg=o ).grid(row=21,sticky=W)
        Label(self, text= 'Setosa:  '+ str(len(controller.banco_dados.setosa[0])),  padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=22,sticky=W)
        Label(self, text= 'Versicolor:  '+ str(len(controller.banco_dados.versicolor[0])), padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=23,sticky=W)
        Label(self, text= 'Virginica:  '+ str(len(controller.banco_dados.virginica[0])),  padx = 30, height=1, anchor='sw', font='Ivi 10 bold',bg=a, fg=o ).grid(row=24,sticky=W)
        Button(self,text="Voltar",bg=a,fg=o,width=15,command= lambda: controller.switchWindows(3,0)).grid(row=25)


        
 
root = Tk()
Controller(root)
root.title("")
root.mainloop()