from FlorestaTrop import FlorestaTropical
from Savana import Savana
from Tundra import Tundra
from Organismo import Organismo
from Pele import Pele
from Utero import Utero

class Sistema():
    def __init__(self):
        self.avatares = []
        self.biomas = []

    def ver_status_saude(self):
        print("\n===== Status de Saúde dos seus Avatares =====\n")
        for avatar in self.avatares:
            print(f"| Nome: {avatar.nome} \n| Idade: {avatar.idade} anos \n| Peso: {avatar.peso} kg \n| Energia: {avatar.energia} \n| Fome: {avatar.fome} \n| Intensidade da dor: {avatar.intensidade_dor}")

    def criar_avatar(self, nome, idade, peso, indice_bioma):
        bioma = self.biomas[indice_bioma]
        self.avatares.append(Organismo(nome, idade, peso, bioma))
    
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
        else:
            print("Opção inválida")
            
    def exibir_dados(self):
        print("\n===== DADOS DO BIOMA =====")
        for bioma in self.biomas:
            bioma.exibir_dados()
            if bioma.nome == "Floresta Tropical":
                print(f"| Umidade relativa: {bioma.umidade_relativa} \n| Densidade da Copada: {bioma.densidade_copada}")
            elif isinstance(bioma, Savana):
                print(f"| Nível de queimada: {bioma.nivel_queimada}")
            elif isinstance(bioma, Tundra):
                print(f"| Espessura da neve: {bioma.espessura_neve}")

    def fazer_funcoes_utero(self):
        for avatar in avatares:
            print(f"Veja os status do útero do avatar {avatar.nome}:")
            avatar.utero.atualizar_tamanho_por_idade()
            avatar.utero.menstruar()
            avatar.utero.verificar_status()

    def fazer_funcoes_pele(self):
        for avatar in avatares:
            print(f"Veja os status da pele do avatar {avatar.nome}:")
            avatar.pele.tomar_sol()
            avatar.pele.sofrer_picadas()
            avatar.pele.enfrentar_frio()### falta organizar por bioma aqui e no organismo