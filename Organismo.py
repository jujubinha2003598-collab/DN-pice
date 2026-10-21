from Bioma import Bioma
from Pele import Pele
from Utero import Utero
from random import randint
from Tundra import Tundra
from FlorestaTrop import FlorestaTropical
from Savana import Savana

class Organismo():
    def __init__(self, nome, idade, peso, energia = 100, intensidade_dor = 0, fome = 0):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.energia = energia
        self.intensidade_dor = intensidade_dor
        self.bioma = Bioma
        self.pele = Pele                                                                                                               , )
        self.utero = Utero
        self.fome = fome

    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        if self.peso >= 70:
            quilos_extras = self.peso - 70
            gasto += gasto * (quilos_extras * 0.01)
        self.energia -= int(gasto)
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")

    def hidratar(self, escolha):
        if escolha == "1":
            self.energia += 10
            print(f"Parabéns, {self.nome}! Você bebeu 200ml de água potável!") 

        elif escolha == "2":
            self.energia += 15 
            print(f"Maravilha! {self.nome} Você bebeu 200ml de água de coco!") 

        elif escolha == "3":
            self.energia -= 15
            print(f"Que nojo! {self.nome} você bebeu 200ml de água suja!") 

        else:
            print("Opção inválida! Você não bebeu nada.")
            self.energia -= 10


    def alimentar(self, escolha):
        if escolha == "1":
            self.energia += 15
            self.fome -= 10 
            print(f"Ops! {self.nome} tinha opção melhor hein.")

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
            print(f"Você está sem energia e com fome. {self.nome} não sobreviveu.")

        elif (self.energia == 0) and (self.fome >= 60):
            print(f"Você está sem energia e com fome. {self.nome} melhor comer e se hidratar.")

    def proteger(self, escolha):
        if escolha == "1":
            if self.bioma == "2" and self.intensidade_dor > 0 or self.bioma == "2":
                self.intensidade_dor -= 1
                print("Parabéns você escolheu certo!")
                
            elif self.bioma == "1" or self.bioma == "3":
                self.intensidade_dor += 1
                print("Você usou o item errado para este bioma!")

        elif escolha == "2":
            if self.bioma == "1" and self.intensidade_dor > 0 or self.bioma == "1":
                self.intensidade_dor -= 1
                print("Parabéns você escolheu certo!")
                
            elif self.bioma == "2" or self.bioma == "3":
                self.intensidade_dor += 1
                print("Você usou o item errado para este bioma!")

        elif escolha == "3":
            if self.bioma == "3" and self.intensidade_dor > 0 or self.bioma == "3":
                self.intensidade_dor -= 1
                print("Parabéns você escolheu certo!")
                
            elif self.bioma == "1" or self.bioma == "2":
                self.intensidade_dor += 1
                print("Você usou o item errado para este bioma!")

        else:
            print("Opção inválida! Você não protegeu nada.")
            self.intensidade_dor += 3

       