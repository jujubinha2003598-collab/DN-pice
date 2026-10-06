from Bioma import Bioma 


class FlorestaTropical(Bioma):

    def __init__(self, umidade_relativa: float = 85.0, densidade_copada: float = 90.0, tipo_solo: str):

        super().__init__(
            nome="Floresta Tropical",
            clima="Equatorial / Tropical Úmido",
            regiao="Amazônia / Bacia do Congo",
            temp_min=22.0,
            temp_max=32.0,
            especificidade="Canópia densa e solo com serrapilheira"
        )
        self.umidade_relativa = umidade_relativa
        self.densidade_copada = densidade_copada
        self.tipo_solo = tipo_solo  

    def gerar_sombra_canopia(self) -> float:
        temp_real = self.calcular_temperatura()
        desconto_termico = (self.densidade_copada / 100) * 3.0
        return round(temp_real - desconto_termico, 1)

