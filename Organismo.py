from Bioma import Bioma
from Pele import Pele
from Utero import Utero

class Organismo:
    def __init__(self, nome, idade, peso, energia, intensidade_dor, bioma, fome):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.energia = 100
        self.intensidade_dor = 0
        self.bioma = bioma
        self.pele = Pele(  ,  )                                                                                                                , )
        self.utero = Utero(10 , )
        self.fome = 0

    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        self.energia -= int(gasto)
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")
        
    def hidratar(self):
        print(f"{self.nome} bebeu 200ml de água!")
        self.energia += 10
    
    def alimentar(self, escolha):
        if escolha == "1":
            self.energia += 15
            self.fome -= 10 
                print("Ops! Você tinha opção melhor hein.")

        elif escolha == "2":
            self.energia += 15
            self.fome -= 10 
            print("Foi quase hein! Boa sorte na próxima.")

        elif escolha == "3":
            self.energia += 15
            self.fome -= 10
            print("Opção incrível!! Parabéns") 

        else:
            print("Opção inválida! Você não comeu nada.")
            self.fome += 15
            self.energia -= 15 

    def ver_status_saude(self):
         print("\n===== Status de Saúde =====\n")
        print(f"| Nome: {self.nome} \n| Idade: {self.idade} anos \n| Peso: {self.peso} kg \n| Energia: {self.energia} \n| Fome: {self.fome} \n| Intensidade da dor: {self.intensidade_dor}")
    
        
    def fazer_nada(self):
        if self.energia > 0 :
            self.energia -= 10
            print(f"Deu mole perdeu energia. Energia atual {self.energia}")
        elif (self.energia == 0) and (self.fome == 100):


            elif :



    def proteger(self, escolha):
        if escolha == "1":
            if bioma == "2" and self.intensidade_dor >= 10:
                self.intensidade_dor -= 5
                print("Parabéns você escolheu certo!")
                
            elif bioma == "1" or bioma == "3":
                self.intensidade_dor -= 5
                print("Ops! Você tinha opção melhor hein.")

        elif escolha == "2":
            self.energia += 15
            self.fome -= 10 
            print("Foi quase hein! Boa sorte na próxima.")

        elif escolha == "3":
            self.energia += 15
            self.fome -= 10
            print("Opção incrível!! Parabéns") 

        else:
            print("Opção inválida! Você não comeu nada.")
            self.fome += 15
            self.energia -= 15 
       