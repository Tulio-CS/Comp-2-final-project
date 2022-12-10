from tkinter import * 
from math import sqrt
from tkinter import messagebox

class Analisar(Frame):
    def __init__(self:object,master: Frame,controller) -> None:
        """Frame que contem as entradas para a classificacao da amostra
        de uma flor"""

        # ---Titulo---
        super().__init__(master,bg="#292929")
        Label(self,text="Insira os dados",bg="#292929",fg="white", font='Ivi 15 bold').grid(row=0,column=0,columnspan=2)
        Label(self,text="",bg="#292929").grid(row=1,column=0,columnspan=2)

        # ---Comprimento da sepala---
        Label(self,text="Comprimento da sepala:",width=20,bg="#292929",fg="white", font='Ivi 10 bold', anchor='sw').grid(row=2,column=0)
        self.com_sep = Entry(self,width=24,bg="#3F3F3F",fg="white")
        self.com_sep.grid(row=2,column=1)

        # ---Largura da sepala---
        Label(self,text="Largura da sepala:",width=20,bg="#292929",fg="white", font='Ivi 10 bold', anchor='sw').grid(row=3,column=0)
        self.lar_sep = Entry(self,width=24,bg="#3F3F3F",fg="white")
        self.lar_sep.grid(row=3,column=1)

        # ---Comprimento da petala---
        Label(self,text="Comprimento da petala:",width=20,bg="#292929",fg="white", font='Ivi 10 bold', anchor='sw').grid(row=4,column=0)
        self.com_pet = Entry(self,width=24,bg="#3F3F3F",fg="white")
        self.com_pet.grid(row=4,column=1)

        # ---Largura da petala---
        Label(self,text="Comprimento da petala:",width=20,bg="#292929",fg="white", font='Ivi 10 bold', anchor='sw').grid(row=5,column=0)
        self.lar_pet = Entry(self,width=24,bg="#3F3F3F",fg="white")
        self.lar_pet.grid(row=5,column=1)

        # ---Botoes---
        Label(self,text="",bg="#292929").grid(row=6,column=0,columnspan=2)
        Button(self,text="Voltar",width=22,bg="#f44336",fg="white",command= lambda: controller.switchWindows(2,0)).grid(row=7,column=0)
    
        Button(self,text="Analisar",width=22,bg="#4CAF50",fg="white",command= lambda: self.analisar(controller)).grid(row=7,column=1)
        self.pack(padx = 0, pady = 0,fill="both",expand=True)
    
    def analisar(self,controller:object) -> object:
        """Função que classifica uma amostra de flor calculando sua distancia euclidiana
        e testando sua compatibilidade"""

        if self.com_pet.get() == "" or self.lar_pet.get() == "" or self.com_sep.get() == "" or self.lar_sep.get() == "":
            # Tratando excecoes 
            messagebox.showerror(message="Não foram inseridas as informaçoes")
        else:

            min_dist_setosa = self.distancia_euclidiana_4D(max(controller.banco_dados.setosa[0]),max(controller.banco_dados.setosa[1]),max(controller.banco_dados.setosa[2]),max(controller.banco_dados.setosa[3]))

            min_dist_virginica = self.distancia_euclidiana_4D(max(controller.banco_dados.virginica[0]),max(controller.banco_dados.virginica[1]),max(controller.banco_dados.virginica[2]),max(controller.banco_dados.virginica[3]))

            min_dist_versicolor = self.distancia_euclidiana_4D(max(controller.banco_dados.versicolor[0]),max(controller.banco_dados.versicolor[1]),max(controller.banco_dados.versicolor[2]),max(controller.banco_dados.versicolor[3]))

            #Calculando a distancia para as flores do tipo setosa
            for i in range(len(controller.banco_dados.setosa[0])):
                dist = self.distancia_euclidiana_4D(controller.banco_dados.setosa[0][i],controller.banco_dados.setosa[1][i],controller.banco_dados.setosa[2][i],controller.banco_dados.setosa[3][i])
                if dist <= min_dist_setosa:
                    min_dist_setosa = dist

            #Calculando a distancia para as flores do tipo versicolor
            for i in range(len(controller.banco_dados.versicolor[0])):
                dist = self.distancia_euclidiana_4D(controller.banco_dados.versicolor[0][i],controller.banco_dados.versicolor[1][i],controller.banco_dados.versicolor[2][i],controller.banco_dados.versicolor[3][i])
                if dist <= min_dist_versicolor:
                    min_dist_versicolor = dist

            #Calculando a distancia para as flores do tipo virginica
            for i in range(len(controller.banco_dados.virginica[0])):
                dist = self.distancia_euclidiana_4D(controller.banco_dados.virginica[0][i],controller.banco_dados.virginica[1][i],controller.banco_dados.virginica[2][i],controller.banco_dados.virginica[3][i])
                if dist <= min_dist_virginica:
                    min_dist_virginica = dist

            #Calculando a compatibilidade e mostrando os resultados
            soma = min_dist_setosa + min_dist_versicolor + min_dist_virginica

            result = "Compatibilidade:\n\nSetosa : {}%\nVersicolor : {}%\nVirginica :{}%".format(round(((1-(min_dist_setosa/soma) )*100), 2),round(((1-(min_dist_versicolor/soma) )*100), 2),round(((1-(min_dist_virginica/soma) )*100), 2))

            messagebox.showinfo("Resultado",result)

        

    def distancia_euclidiana_4D(self,x:float,y:float,z:float,w:float) -> float:
        """
           Eixo x = comprimento sepala
           Eixo y = largira sepala
           Eixo z = comprimento petala
           Eixo w = largura petala
        """
        dist = sqrt(((float(self.com_sep.get()) - x) ** 2) + ((float(self.lar_sep.get()) - y) ** 2) + ((float(self.com_pet.get()) - z) ** 2) + ((float(self.lar_pet.get()) - w) ** 2))
        return dist


