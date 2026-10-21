from Organismo import Organismo
import random 

class Pele():
    def __init__(self, melanina):
        self.melanina = melanina
        self.verificar_protecao = False
 
    def tomar_sol(self):
        if self.melanina == "baixa":
            print("Você está tomando sol, mas sua pele é sensível. Cuidado com queimaduras!")
            self.verificar_protecao = True
        elif self.melanina == "media":
            print("Você está tomando sol, sua pele tem proteção moderada.")
            self.verificar_protecao = True
        elif self.melanina == "alta":
            print("Você está tomando sol, sua pele tem alta proteção natural.")
            self.verificar_protecao = True