from Bioma import Bioma

class Savana(Bioma):
    def __init__(self, nivel_queimada: int):
        super().__init__(
            nome="Savana",
            clima="Tropical Semiárido",
            regiao="África / América do Sul",
            temp_min=20.0,
            temp_max=40.0,
            especificidade="Estação seca prolongada",
            tipo_solo="Arenoso e poroso (Pobre em nutrientes)" 
        )
        self.nivel_queimada = nivel_queimada