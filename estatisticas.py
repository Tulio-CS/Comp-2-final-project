
from tkinter import *
import numpy as np

class Estatisticas(Frame):
    def __init__(self,master,controller):
        super().__init__(master,bg="#292929")
        o = 'white'
        a = '#292929'
        Button(self,text="Voltar",bg=a,fg=o,width=15,command= lambda: controller.switchWindows(3,0)).grid(row=25)
        try:
            comprimento_sepala = np.concatenate((controller.banco_dados.setosa[0],controller.banco_dados.versicolor[0],controller.banco_dados.virginica[0]))
            largura_sepala = np.concatenate((controller.banco_dados.setosa[1],controller.banco_dados.versicolor[1],controller.banco_dados.virginica[1]))
            comprimento_petala = np.concatenate((controller.banco_dados.setosa[2],controller.banco_dados.versicolor[2],controller.banco_dados.virginica[2]))
            largura_petala = np.concatenate((controller.banco_dados.setosa[3],controller.banco_dados.versicolor[3],controller.banco_dados.virginica[3]))
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
        except ValueError:
            pass