from Organismo import Organismo
import random 

class Pele(Organismo):
    def __init__(self, nome, idade, peso, bioma):
        super().__init__(nome, idade, peso, 100, 0, bioma)

    def proteger(self):
        pass