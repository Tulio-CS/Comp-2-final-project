#Trabalho Final de Computação
#Alunos: Jhulia Schmidt Ceccon, Pedro Henrique Chicarino, Túlio Castro Silva
#Professor : Giomar

from tkinter import Button,Frame,Tk
from tkinter.filedialog import askopenfilename
from estatisticas import Estatisticas
import pickle



class menu(Frame):
    def __init__(self, master:Tk,controller:object) -> None:
        super().__init__(master,bg="#292929")
     
        # ---Botao para mostrar as estatisticas---
        Button(self,text="Mostrar estatisticas",bg="#025773",fg="white", height=8,width=16 ,font='Ivi 10 bold',command=lambda: controller.switchWindows(0,3)).grid(row=1,column=0)

        # ---Botao para plotar graficos---
        Button(self,text="Mostrar graficos",bg="#006666",fg="white", height=8,width=16 , font='Ivi 10 bold',command= lambda: controller.switchWindows(0,1)).grid(row=1,column=1)

        # ---Botao para classificar uma amostra---
        Button(self,text="Classificar amostra",bg="#C6093B",fg="white",height=8,width=16, font='Ivi 10 bold',command= lambda: controller.switchWindows(0,2)).grid(row=1,column=2)

        # ---Botao para selecionar o caminho---
        Button(self,text="Alterar o caminho",bg="#292929",fg="white",border = 0, font='Ivi 10 bold', command=lambda: self.choose_path(master,controller)).grid(row=2,column=0,pady=10)
        
        # ---Botao para sair do progama---
        Button(self,text="Sair",bg="#292929",fg="white",border = 0, font='Ivi 10 bold', command= lambda: self.sair(controller)).grid(row=2,column=2)


        self.pack()
    
    def choose_path(self,master:Tk,controller:object) -> None:
        """Funcao que escolhe o caminho para o arquivo .csv contendo os dados"""

        file = askopenfilename(filetypes = (("CSV Files","*.csv"),))

        if len(file) != 0: #Tratando as excecoes

            controller.path = file
            controller.banco_dados.path = file
            controller.banco_dados.rotina_csv()

            controller.path_label.config(text = file)

            del controller.framelist[3]

            page_estatisticas = Estatisticas(master,controller)
            
            controller.framelist.append(page_estatisticas)




    def sair(self,master:Tk) -> None:
        """Funcao que encerra o progama"""
        with open("data.pkl","wb") as file:
            pickle.dump(master.path,file)
        master.master.destroy()

