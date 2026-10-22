from Organismo import Organismo
import random 

class Utero():
    def __init__(self, organismo, tamanho_utero = 10, saude =  10):
        self.organismo = organismo
        self.tamanho_utero = self.tamanho_utero
        self.saude = self.saude

    def atualizar_tamanho_por_idade(self):
        if self.organismo.idade < 12:
            self.tamanho_utero = 5  
        elif self.organismo.idade > 55:
            self.tamanho_utero = 7  
        else:
            self.tamanho_utero = 10 

    def menstruar(self):
        if self.organismo.idade >= 12 and self.organismo.idade <= 55:
            
            if self.organismo.fome >= 60 or self.organismo.energia <= 40:
                self.saude -= 2
                print("Cuidado! você tem um índice de saúde baixo.")
                
            else:
                self.saude = self.saude
                print("Você está menstruando normalmente!")
                
        else:
            self.saude = 10
            print("Você não está na idade fértil.")

    def verificar_status(self):
        print("--- Status do Útero ---")
        print(f"Tamanho do útero: {self.tamanho_utero}")
        print(f"Saúde do útero: {self.saude}")

        if self.saude <= 4:
            print("Estado crítico!")
        elif self.saude <= 7:
            print("Estado de atenção.")
        else:
            print("Estado saudável.")
        
        idade = self.organismo.idade
        if idade < 12:
            print("Você ainda não passou pela menarca garotinha!")
        elif idade > 55:
            print("Você está na fase pós-menopausa")
        else:
            print("Que útero abençoado! Está super fértil")

    
