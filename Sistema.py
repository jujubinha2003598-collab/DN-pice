class Sistema():
    def __init__(self):
        self.avatares = []
        self.biomas = []

    def ver_status_saude(self):
        print("\n===== Status de Saúde dos seus Avatares =====\n")
        for avatar in self.avatares:
            print(f"| Nome: {avatar.nome} \n| Idade: {avatar.idade} anos \n| Peso: {avatar.peso} kg \n| Energia: {avatar.energia} \n| Fome: {avatar.fome} \n| Intensidade da dor: {avatar.intensidade_dor}")
        
    def criar_bioma(self, escolha):
        if escolha == 1:#floresta tropical
            tipo_solo = input("Informe o tipo do solo:")
            obj_bioma_ft = FlorestaTropical(tipo_solo)#cria o bioma
            self.biomas.append(obj_bioma_ft)#adiciona na lista de biomas

        elif escolha == 2:#Savana
            nivel_queimada = int(input("Informe o nivel de queimada:"))
            obj_bioma_s = Savana(nivel_queimada)#cria o bioma
            self.biomas.append(obj_bioma_s)#adiciona na lista de biomas

        elif escolha == 3:#Tundra
            espessura_neve = int(input("Informe a espessura da neve:"))
            obj_bioma_t = Tundra(espessura_neve)#cria o bioma
            self.biomas.append(obj_bioma_t)#adiciona na lista de biomas