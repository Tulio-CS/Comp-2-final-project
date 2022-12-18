#Trabalho Final de Computação
#Alunos: Jhulia Schmidt Ceccon, Pedro Henrique Chicarino, Túlio Castro Silva
#Professor : Giomar

import numpy as np
import csv
from tkinter import messagebox


class banco_de_dados:
    def __init__(self,path:str) -> None:
        """Objeto que guarda os valores referentes ao 
        comprimento da selapa , largura da sepala
        comprimento da petala, largura da petala
        de cada tipo de flor"""
        self.path = path
        self.setosa = np.array([[],[],[],[]])
        self.versicolor = np.array([[],[],[],[]])
        self.virginica = np.array([[],[],[],[]])
            
    def rotina_csv(self) -> None:
        """Rotina que atualiza o banco de dados com os valores
        do arquivo .csv inserido no caminho(path)"""
        try:
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
        except FileNotFoundError:
            if len(self.path) != 0:
                messagebox.showerror('Python Error', 'Error: Caminho invalido')


