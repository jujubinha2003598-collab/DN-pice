from Bioma import Bioma
import random 
class Savana(Bioma):
    item_correto = 1
    def __init__(self, nivel_queimada: int):
        super().__init__(
            nome="Savana",
            clima="Tropical Semiárido",
            regiao="África / América do Sul",
            temp_min=20.0,
            temp_max=40.0,
            especificidade="Estação seca prolongada",
            tipo_solo="Arenoso e poroso (Pobre em nutrientes)" 
        )
        self.nivel_queimada = nivel_queimada
    
    def calcular_temperatura(self) -> float:
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        temperatura_atual += self.nivel_queimada * 1.5
        return round(temperatura_atual, 1)
    
    def dificuldade_solo(self) -> float:
        return 1.2 + self.nivel_queimada * 0.1

 
    def aplicar_efeito_pele(self, organismo, usou_item_certo):
        organismo.pele.tomar_sol(tem_protetor_solar=usou_item_certo, bioma=self.nome)
