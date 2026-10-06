from abc import ABC, abstractmethod
import random 

class Bioma(ABC):

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

    def exibir_dados(self):
        temp_atual = self.calcular_temperatura()
        print("\n===== DADOS DO BIOMA =====")
        print(f"| Nome: {self.nome} \n| Temperatura: {temp_atual}°C \n| Clima: {self.clima} \n| Região: {self.regiao} \n| Especificidade: {self.especificidade} \n| Tipo do solo: {self.tipo_solo }")

 