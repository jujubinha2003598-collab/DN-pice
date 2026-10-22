from Bioma import Bioma 
import random 

class FlorestaTropical(Bioma):

    item_correto = 2
    
    def __init__(self, tipo_solo: str, umidade_relativa: float = 85.0, densidade_copada: float = 90.0):
        super().__init__(
            nome="Floresta Tropical",
            clima="Equatorial / Tropical Úmido",
            regiao="Amazônia / Bacia do Congo",
            temp_min=22.0,
            temp_max=32.0,
            especificidade="Canópia densa e solo com serrapilheira",
            tipo_solo=tipo_solo
            )
        self.umidade_relativa = umidade_relativa
        self.densidade_copada = densidade_copada

    def gerar_sombra_canopia(self):
        temp_real = self.calcular_temperatura()
        desconto_termico = (self.densidade_copada / 100) * 3.0
        return round(temp_real - desconto_termico, 1)

    def calcular_temperatura(self):
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        return round(temperatura_atual, 1)

    def dificuldade_solo(self):
        return 0.5 + (self.umidade_relativa / 100) * 0.3

    def aplicar_efeito_pele(self, organismo, usou_item_certo):
        organismo.pele.sofrer_picadas(tem_repelente=usou_item_certo)

