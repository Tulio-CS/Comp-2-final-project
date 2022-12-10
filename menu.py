from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from estatisticas import Estatisticas
import pickle


class menu(Frame):
    def __init__(self, master:Tk,controller:object) -> None:
        super().__init__(master,bg="#292929")

        # ---Label indicando o caminho---
        self.path_label = Label(self,text="{}".format(controller.path),bg="#292929",fg="red", font='Ivi 7 bold', anchor='sw')
        self.path_label.pack()

        # ---Botao para selecionar o caminho---
        Button(self,text="Selecionar caminho para arquivo",bg="#191919",fg="white", height=1, font='Ivi 10 bold', anchor='sw', command=lambda: self.choose_path(master,controller)).pack(fill="both",expand=True)

        # ---Botao para mostrar as estatisticas---
        Button(self,text="Mostrar estatisticas",width=15,bg="#191919",fg="white",  height=1, font='Ivi 10 bold', anchor='sw',command=lambda: controller.switchWindows(0,3)).pack(fill="both",expand=True)

        # ---Botao para plotar graficos---
        Button(self,text="Mostrar graficos",width=15,bg="#191919",fg="white", height=1, font='Ivi 10 bold', anchor='sw',command= lambda: controller.switchWindows(0,1)).pack(fill="both",expand=True)

        # ---Botao para classificar uma amostra---
        Button(self,text="Classificar amostra",width=15,bg="#191919",fg="white",  height=1, font='Ivi 10 bold', anchor='sw',command= lambda: controller.switchWindows(0,2)).pack(fill="both",expand=True)
        
        # ---Botao para sair do progama---
        Button(self,text="Sair",width=15,bg="#191919",fg="white",  height=1, font='Ivi 10 bold', anchor='sw', command= lambda: self.sair(controller)).pack(fill="both",expand=True)
        self.pack(padx = 0, pady = 0,fill="both",expand=True)
    
    def choose_path(self,master:Tk,controller:object) -> None:
        """Funcao que escolhe o caminho para o arquivo .csv contendo os dados"""

        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))

        if len(file) != 0: #Tratando as excecoes

            controller.path = file
            controller.banco_dados.path = file
            controller.banco_dados.rotina_csv()

            self.path_label.config(text="caminho: \n{}\n".format(controller.path))

            del controller.framelist[3]

            page_estatisticas = Estatisticas(master,controller)
            
            controller.framelist.append(page_estatisticas)




    def sair(self,master:Tk) -> None:
        """Funcao que encerra o progama"""
        with open("data.pkl","wb") as file:
            pickle.dump(master.path,file)
        master.master.destroy()

