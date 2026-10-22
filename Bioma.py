from abc import ABC, abstractmethod
import random 

class Bioma(ABC):

    item_correto = None

    def __init__(self, nome: str, clima: str, regiao: str, temp_min: float, temp_max: float, especificidade: str, tipo_solo):
        self.nome = nome
        self.clima = clima
        self.regiao = regiao
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.especificidade = especificidade
        self.tipo_solo = tipo_solo

    @abstractmethod
    def calcular_temperatura(self):
        pass
    
    @abstractmethod
    def dificuldade_solo(self):
        pass
    
    def proteger(self, organismo, escolha):
        if escolha == self.item_correto:
            organismo.intensidade_dor = max(0, organismo.intensidade_dor - 1)
            print(f"Parabéns, {organismo.nome}! Você se protegeu na {self.nome}!")
        else:
            organismo.intensidade_dor += 1
            print(f"Você usou o item errado! Sua dor aumentou na {self.nome}.")

    def exibir_dados(self):
        temp_atual = self.calcular_temperatura()
        print("\n===== DADOS DO BIOMA =====")
        print(f"| Nome: {self.nome} |")
        print(f'| Temperatura: {temp_atual}°C |')
        print(f'| Clima: {self.clima} | ')
        print(f'| Região: {self.regiao} | ')
        print(f'| Especificidade: {self.especificidade} | ')
        print(f'| Tipo do solo: {self.tipo_solo } |')
 
