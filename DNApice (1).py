class Coracao:
    def __init__(self):
        self.frequenciaCardiaca = 70 # bpm

    def acelerar(self):
        self.frequenciaCardiaca += 20

    def desacelerar(self):
        self.frequenciaCardiaca -= 10

    def mostrarStatus(self):
        print(f"Frequência Cardíaca: {self.frequenciaCardiaca}")

class Pulmao:
    def __init__(self):
        self.oxigenacao = 98 # %

    def respirarMaisRapido(self):
        if self.oxigenacao < 100:
            self.oxigenacao += 1

    def mostrarStatus(self):
        print(f"Oxigenação: {self.oxigenacao}")

class Organismo:
    def __init__(self, nome, bioma):
        self.nome = nome
        self.bioma = bioma
        self.hidratacao = 100
        self.temperatura = 36.5
        self.coracao = Coracao()
        self.pulmao = Pulmao()

    def correr(self):
        print("🏃 O organismo começou a correr...")
        self.coracao.acelerar()
        self.pulmao.respirarMaisRapido()

    def ficarNoSol(self): # Tentar mexer aqui de acordo com a pesquisa
        print("☀️ O organismo está exposto ao calor!")
        self.hidratacao -= 15
        self.temperatura += 0.5

    def beberAgua(self):
        print("💧 O organismo bebeu água!")
        self.hidratacao += 20

    def mostrarStatus(self):
        print("\n===== STATUS DO ORGANISMO =====")
        print(f"Nome: {self.nome} (Bioma {self.bioma.nome})")
        print(f"Hidratação: {self.hidratacao}%")
        print(f"Temperatura: {self.temperatura} ºC")
        self.coracao.mostrarStatus()
        self.pulmao.mostrarStatus()

class Bioma:
    def __init__(self, nome, temperatura):
        self.nome = nome
        self.temperatura = temperatura

    def mostrarStatus(self):
        print("\n===== STATUS DO BIOMA =====")
        print(f"Nome: {self.nome} ({self.temperatura}º C)") 

ambiente = Bioma("Caatinga", 38)
ambiente.mostrarStatus()

avatar = Organismo("Saitama", ambiente)
avatar.mostrarStatus()
avatar.correr()
avatar.ficarNoSol()
avatar.mostrarStatus()
avatar.beberAgua()
avatar.mostrarStatus()