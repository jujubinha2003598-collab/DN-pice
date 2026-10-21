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
    

    def tomar_sol(self, tem_protetor_solar=False):
        print("Você está na Savana tomando sol...")
        if self.melanina == "baixa":
            if tem_protetor_solar:
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.verificar_protecao = True
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.verificar_protecao = False

        elif self.melanina == "média":
            if tem_protetor_solar:
                print("✨ Com protetor solar, sua pele está super protegida!")
                self.verificar_protecao = True
            else:
                print("Você tem proteção moderada, mas o sol da Savana é forte. Cuidado com o tempo de exposição.")
                self.verificar_protecao = True 

        elif self.melanina == "alta":
            print("✨ Sua pele tem alta proteção natural contra os raios da Savana!")
            self.verificar_protecao = True 
