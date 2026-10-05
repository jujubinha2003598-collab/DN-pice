from abc import ABC, abstractmethod

class Bioma(ABC):
    def __init__(self, nome, temperatura_med, clima, regiao, especificidade):
        self.nome = nome
        self.temperaturaMed = temperatura_med
        self.clima = clima
        self.regiao = regiao
        self.especificidade = especificidade

    def exibir_dados(self):
        print("\n===== DADOS DO BIOMA =====")
        print(f"Nome: {self.nome} |  Temp: {self.temperaturaMed}°C | Clima: {self.clima} | Região: {self.regiao} | ") 
    
    @abstractmethod
    def calcular_temperatura(self):
        pass
