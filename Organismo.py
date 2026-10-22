from Bioma import Bioma
from Pele import Pele
from Utero import Utero
from random import randint, random
from Tundra import Tundra
from FlorestaTrop import FlorestaTropical
from Savana import Savana

class Organismo():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.energia = 100
        self.intensidade_dor = 0
        self.bioma = Bioma()
        self.pele = Pele (melanina = random.choice(["baixa", "média", "alta"])) 
        self.utero = Utero(self)
        self.fome = 0


    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        if self.peso >= 70:
            quilos_extras = self.peso - 70
            gasto += gasto * (quilos_extras * 0.01)
        self.energia -= int(gasto)
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")


    def hidratar(self, escolha):
        if escolha == 1:
            self.energia += 10
            print(f"Parabéns, {self.nome}! Você bebeu 200ml de água potável!") 

        elif escolha == 2:
            self.energia += 15 
            print(f"Maravilha! {self.nome} Você bebeu 200ml de água de coco!") 

        elif escolha == 3:
            self.energia -= 15
            print(f"Que nojo! {self.nome} você bebeu 200ml de água suja!") 

        else:
            print("Opção inválida! Você não bebeu nada.")
            self.energia -= 10


    def alimentar(self, escolha):
        if escolha == 1:
            self.energia -= 15
            self.fome += 5 
            print(f"Ops! {self.nome} tinha opção melhor hein.")

        elif escolha == 2:
            self.energia += 5
            self.fome -= 5
            print("Foi quase hein! Boa sorte na próxima.")

        elif escolha == 3:
            self.energia += 15
            self.fome -= 10
            print("Opção incrível!! Parabéns") 

        else:
            print("Opção inválida! Você não comeu nada.")
            self.fome += 15
            self.energia -= 15 
    
        
    def fazer_nada(self):
        if self.energia >=10 :
            self.energia -= 10
            print(f"Deu mole, perdeu energia. Energia atual {self.energia}")

        elif (self.energia == 0) and (self.fome == 100):
            print(f"Você está sem energia e com muita fome. {self.nome} não sobreviveu.")

        elif (self.energia == 0) and (self.fome <= 60):
            print(f"Você está sem energia e com fome. {self.nome} melhor comer e se hidratar.")
            

    def proteger(self, escolha):
        if escolha == 1:
            if self.bioma == 2: # Savana
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você usou o protetor solar e protegeu a pele na Savana!")

            elif self.bioma == 1: # Floresta Tropical
                self.intensidade_dor += 1
                print("Você usou o item errado! Muitas picadas de mosquito na Floresta Tropical aumentaram sua dor.")

            elif self.bioma == 3: # Tundra
                self.intensidade_dor += 1
                print("Você usou o item errado! O frio da Tundra aumentou sua dor.")

        elif escolha == 2:
            if self.bioma == 1: # Floresta Tropical
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você usou o repelente e afastou os insetos da Floresta Tropical!")

            elif self.bioma == 2: # Savana
                self.intensidade_dor += 1
                print("Você usou o item errado! O sol da Savana aumentou sua dor.")

            elif self.bioma == 3: # Tundra
                self.intensidade_dor += 1
                print("Você usou o item errado! O frio da Tundra aumentou sua dor.")

        elif escolha == 3:
            if self.bioma == 3: # Tundra
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você vestiu a blusa de frio e se aqueceu na Tundra!")

            elif self.bioma == 1: # Floresta Tropical
                self.intensidade_dor += 1
                print("Você usou o item errado! Muitas picadas de mosquito na Floresta Tropical aumentaram sua dor.")

            elif self.bioma == 2: # Savana
                self.intensidade_dor += 1
                print("Você usou o item errado! O calor escaldante da Savana aumentou sua dor.")

        else:
            print("Opção inválida! Você não se protegeu.")
            self.intensidade_dor += 3

       
