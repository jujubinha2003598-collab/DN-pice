from Organismo import Organismo
import random 

class Utero():
    def __init__(self, tamanho_utero,  ):
        self.tamanho_utero = 10


    def menstruar(self):
        if self.organismo.idade >= 12 and self.organismo.idade <= 55:

            problemas = 0

            if self.organismo.fome <= 80:

                problemas += 1

            if self.organismo.energia <= 40:

                problemas += 1

            if problemas == 2:
                print("Você não está menstruando! Você está com fome, sem energia . Sem condições de saúde.")
                
            elif problemas == 1:
                print("Você está menstruando, mas cuidado: você tem um índice de saúde baixo.")
                
            else:
                print("Você está menstruando normalmente e sua saúde está perfeita!")
        else:
            print("Você não está menstruando, pois não está na idade fértil.")
