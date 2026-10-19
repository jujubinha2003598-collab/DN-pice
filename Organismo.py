from Bioma import Bioma
from Pele import Pele
class Organismo:
    def __init__(self, nome, idade, peso, energia, intensidade_dor, bioma, fome):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.energia = 100
        self.intensidade_dor = 0
        self.bioma = bioma
        self.pele = Pele(200, )
        self.utero = Utero( , )
        self.fome = 100

    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        self.energia -= int(gasto)
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")
        
    def hidratar(self, quantidade: str):
        print(f"{self.nome} bebeu  ({quantidade}) ml de água!")
        self.energia += 10
    
    def alimentar(self, quantidade: str):
        print(f"{self.nome} alimentou-se com {quantidade}!")
        self.energia += 15    

    def ver_status_saude(self):
