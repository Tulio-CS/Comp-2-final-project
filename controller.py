from tkinter import *
from banco_dados import banco_de_dados
from menu import menu
from plotagem import graph
from analise import Analisar
from estatisticas import Estatisticas
import pickle


class Controller:
    def __init__(self,master: Tk) -> None:
        """Classe que gerencia e armazena todos os dados utilizados no progama
        como o objeto banco de dados, os frames referentes as paginas e o caminho
        para o arquivo .csv"""
        master.configure(bg="#292929")
        mainframe = Frame(master,bg="#292929")
        mainframe.pack(padx=10, pady=10, fill='both', expand=True)
        self.master = master
        
        # Abrindo o caminho que foi salvo anteriormente (se houver)
        try:

            with open("data.pkl","rb") as file: 
                self.path = pickle.load(file)

        except FileNotFoundError:
            self.path = ""
        
        
        #Criando e atualiazndo o banco de dados
        self.banco_dados = banco_de_dados(self.path)
        self.banco_dados.rotina_csv()
        self.framelist = []

        #Criando as frames do progama
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
        if self.path == "":
            self.path_label = Label(master,text="Caminho Invalido",bg="#292929",fg="white")
        else:
            self.path_label = Label(master,text=self.path,bg="#292929",fg="white")
        self.path_label.pack()

    def switchWindows(self,atual:int,proxima:int)  -> None:
        """Função que troca a pagina que e mostrada ao usuario"""
        self.framelist[atual].forget()
        self.framelist[proxima].tkraise()
        self.framelist[proxima].pack(padx = 10, pady = 10)