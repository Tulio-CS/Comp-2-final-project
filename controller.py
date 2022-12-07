from tkinter import *
from banco_dados import banco_de_dados
from menu import menu
from plotagem import graph
from analise import Analisar
from estatisticas import Estatisticas
import pickle
class Controller:
    def __init__(self,master):
        master.configure(bg="#292929")
        mainframe = Frame(master,bg="#292929")
        mainframe.pack(padx=10, pady=10, fill='both', expand=True)
        self.master = master
        self.path = ""
        try:
            with open("data.pkl","rb") as file: 
                self.path = pickle.load(file)
        except FileNotFoundError:
            pass
        self.banco_dados = banco_de_dados(self.path)
        self.banco_dados.rotina_csv()
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