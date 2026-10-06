from abc import ABC, abstractmethod
import random 

class Bioma(ABC):

    def __init__(self, nome: str, clima: str, regiao: str, temp_min: float, temp_max: float, especificidade: str):
        self.nome = nome
        self.clima = clima
        self.regiao = regiao
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.especificidade = especificidade

    def calcular_temperatura(self) -> float:
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        return round(temperatura_atual, 1)

    def exibir_dados(self):
        temp_atual = self.calcular_temperatura()
        print("\n===== DADOS DO BIOMA =====")
        print(f"Nome: {self.nome} | Temperatura: {temp_atual}°C | Clima: {self.clima} | Região: {self.regiao} | Especificidade: {self.especificidade}")

    """ @abstractmethod
    def calcular_temperatura(self):
        pass
    """