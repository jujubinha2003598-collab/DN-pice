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
    

    def tomar_sol(self, tem_protetor_solar=False):######vai ficar com qual????#até então usei esse
        print("Você está na Savana tomando sol...")#funciona nos outros biomas tbmm ou não??
        if self.melanina == "baixa":
            if tem_protetor_solar == True:#esse é muito bom só teria q atualizar essa variável tbm
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.verificar_protecao = True
                
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.verificar_protecao = False

        elif self.melanina == "média":
            if tem_protetor_solar == True:###
                print("✨ Com protetor solar, sua pele está super protegida!")
                self.verificar_protecao = True
            else:
                print("Você tem proteção moderada, mas o sol da Savana é forte. Cuidado com o tempo de exposição.")
                self.verificar_protecao = True 

        elif self.melanina == "alta":
            print("✨ Sua pele tem alta proteção natural contra os raios da Savana!")
            self.verificar_protecao = True









import random 

class Pele():
    def __init__(self, melanina):
        self.melanina = melanina
        self.protecao = False
    

    def tomar_sol(self, tem_protetor_solar=False):
        if self.melanina == "baixa":
            if tem_protetor_solar:#esse é muito bom só teria q atualizar essa variável tbm
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.protecao = True
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.protecao = False

        elif self.melanina == "media":
            if tem_protetor_solar:
                print("✨ Com protetor solar, sua pele está super protegida!")
                self.protecao = True###
            else:
                print("Você tem proteção moderada, mas o sol da Savana é forte. Cuidado com o tempo de exposição.")
                self.protecao = True 

        elif self.melanina == "alta":
            print("✨ Sua pele tem alta proteção natural contra os raios da Savana!")
            self.protecao = True 

    def sofrer_picadas(self, tem_repelente=False):
        if tem_repelente:
            print(" O repelente afastou os mosquitos!")
            self.protecao = True
        else:
            print("Você foi picado várias vezes!")
            self.protecao = False

    def enfrentar_frio(self, tem_blusa=False):
        if tem_blusa:
            print(" A blusa de frio manteve sua pele aquecida!")
            self.protecao = True
        else:
            print(" Sua pele está ressecando e congelando!")
            self.protecao = False
