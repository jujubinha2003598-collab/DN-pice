from Organismo import Organismo
import random 

class Utero(Organismo):
    def __init__(self, nome, idade, peso, bioma):
        super().__init__(nome, idade, peso, bioma)

    def menstruar(self):
        pass