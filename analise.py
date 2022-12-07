from tkinter import * 
from math import sqrt
from tkinter import messagebox

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
        min_dist_setosa = self.distancia_euclidiana_4D(max(controller.banco_dados.setosa[0]),max(controller.banco_dados.setosa[1]),max(controller.banco_dados.setosa[2]),max(controller.banco_dados.setosa[3]))
        min_dist_virginica = self.distancia_euclidiana_4D(max(controller.banco_dados.virginica[0]),max(controller.banco_dados.virginica[1]),max(controller.banco_dados.virginica[2]),max(controller.banco_dados.virginica[3]))
        min_dist_versicolor = self.distancia_euclidiana_4D(max(controller.banco_dados.versicolor[0]),max(controller.banco_dados.versicolor[1]),max(controller.banco_dados.versicolor[2]),max(controller.banco_dados.versicolor[3]))
        classificacao = "Sem classificação"
        for i in range(len(controller.banco_dados.setosa[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.setosa[0][i],controller.banco_dados.setosa[1][i],controller.banco_dados.setosa[2][i],controller.banco_dados.setosa[3][i])
            if dist <= min_dist_setosa:
                min_dist_setosa = dist
        for i in range(len(controller.banco_dados.versicolor[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.versicolor[0][i],controller.banco_dados.versicolor[1][i],controller.banco_dados.versicolor[2][i],controller.banco_dados.versicolor[3][i])
            if dist <= min_dist_versicolor:
                min_dist_versicolor = dist
        for i in range(len(controller.banco_dados.virginica[0])):
            dist = self.distancia_euclidiana_4D(controller.banco_dados.virginica[0][i],controller.banco_dados.virginica[1][i],controller.banco_dados.virginica[2][i],controller.banco_dados.virginica[3][i])
            if dist <= min_dist_virginica:
                min_dist_virginica = dist
        soma = min_dist_setosa + min_dist_versicolor + min_dist_virginica
        result = "Setosa : {}%\nVersicolor : {}%\nVirginica :{}%".format(round(((1-(min_dist_setosa/soma) )*100), 2),round(((1-(min_dist_versicolor/soma) )*100), 2),round(((1-(min_dist_virginica/soma) )*100), 2))
        messagebox.showinfo("Resultado",result)
        print(result)
        

    def distancia_euclidiana_4D(self,x,y,z,w):
        """Eixo x = comprimento sepala
           Eixo y = largira sepala
           Eixo z = comprimento petala
           Eixo w = largura petala"""
        dist = sqrt(((float(self.com_sep.get()) - x) ** 2) + ((float(self.lar_sep.get()) - y) ** 2) + ((float(self.com_pet.get()) - z) ** 2) + ((float(self.lar_pet.get()) - w) ** 2))
        return dist