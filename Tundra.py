from Bioma import Bioma 
import random 

class Tundra(Bioma):    

    item_correto = 3
    
    def __init__(self, espessura_neve: float = 20.0):
        super().__init__(
            nome="Tundra", 
            clima="Frio Polar", 
            regiao="Ártico", 
            temp_min=-20.0, 
            temp_max=0.0, 
            especificidade="Periglacial", 
            tipo_solo="Permafrost" 
        )
        self.espessura_neve = espessura_neve
        
    def calcular_temperatura(self) -> float:
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        return round(temperatura_atual, 1)

    def dificuldade_solo(self):
        return 1.5 + (self.espessura_neve / 100) * 0.5
    
