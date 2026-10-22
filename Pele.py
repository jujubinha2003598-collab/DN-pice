import random 

class Pele():
    def __init__(self, melanina):
        self.melanina = melanina
        self.protecao = False
    

    def tomar_sol(self, tem_protetor_solar=False):
        if self.melanina == "baixa":
            if tem_protetor_solar:
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.protecao = True
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.protecao = False

        elif self.melanina == "media":
            if tem_protetor_solar:
                print("✨ Com protetor solar, sua pele está super protegida!")
                self.protecao = True
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