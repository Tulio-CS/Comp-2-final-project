from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from estatisticas import Estatisticas
import pickle


class menu(Frame):
    def __init__(self, master,controller):
        super().__init__(master,bg="#292929")
        self.path_label = Label(self,text="caminho :{}".format(controller.path),bg="#292929",fg="white")
        self.path_label.pack()
        Button(self,text="Selecionar caminho para arquivo .csv",bg="#3F3F3F",fg="white",command=lambda: self.choose_path(master,controller)).pack(fill="both",expand=True)
        Button(self,text="Mostrar estatisticas",width=15,bg="#3F3F3F",fg="white",command=lambda: controller.switchWindows(0,3)).pack(fill="both",expand=True)
        Button(self,text="Mostrar graficos",width=15,bg="#3F3F3F",fg="white",command= lambda: controller.switchWindows(0,1)).pack(fill="both",expand=True)
        Button(self,text="Classificar amostra",width=15,bg="#3F3F3F",fg="white",command= lambda: controller.switchWindows(0,2)).pack(fill="both",expand=True)
        Button(self,text="sair",width=15,bg="#3F3F3F",fg="white",command= lambda: self.sair(controller)).pack(fill="both",expand=True)
        self.pack(padx = 1, pady = 1,fill="both",expand=True)
    
    def choose_path(self,master,controller):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if len(file) != 0:
            controller.path = file
            controller.banco_dados.path = file
            controller.banco_dados.rotina_csv()
            self.path_label.config(text="caminho :{}".format(controller.path))
            del controller.framelist[3]
            page_estatisticas = Estatisticas(master,controller)
            controller.framelist.append(page_estatisticas)




    def sair(self,master):
        with open("data.pkl","wb") as file:
            pickle.dump(master.path,file)
        master.master.destroy()

