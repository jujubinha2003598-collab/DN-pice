#main
import random
from Bioma import Bioma
from FlorestaTrop import FlorestaTropical
from Savana import Savana
from Tundra import Tundra
from Organismo import Organismo
from Pele import Pele 
from Utero import Utero
from Sistema import Sistema

sistema = Sistema()

print("Seja bem vindo(a) ao nosso Jogo do DNÁpice! \n Escolha seu bioma, avatar, e viva uma aventura cheia de aprendizados!")

while True:
        play = input("Deseja dar play na rodada? (s/n)")
        if play == 's':
                opcao = int(input("O que deseja fazer? \n1)Criar um avatar \n2)Ver status do avatar \n3)Escolher um bioma \n4)Ver status do bioma \n5)Fazer nada (POR FAVOR, APENAS SE O SEU AVATAR EXISTIR) \n6)Alimentar \n7)Hidratar \n8)Proteger \n9) Movimentar \n10)Sair"))

                if opcao == 1:
                        nome = input("Dê um nome:")
                        idade = input("Informe a idade:")
                        peso = input("Informe o peso:")
                        obj_avatar = Organismo(nome, idade, peso)#criando o avatar
                        sistema.avatares.append(obj_avatar)#adicionando o avatar criado na lista de avatares
                        print("Avatar criado com sucesso!")

                elif opcao == 2:
                        sistema.ver_status_saude()

                elif opcao == 3:
                        print("\n--- Biomas ---\n")
                        print("1. Floresta Tropical")
                        print("2. Savana")
                        print("3. Tundra")
                        escolha = int(input("Escolha o número do seu bioma:"))
                        sistema.criar_bioma(escolha)

                elif opcao == 4:
                        sistema.exibir_dados_bioma()
                        
                elif opcao == 5:
                        indice = int(input("Informe o índice do seu avatar:"))
                        confirmacao = sistema.avatares[indice]#procura qual é o avatar que o usuário quer, e coloca esse obj_avatar na variável confirmacao
                        confirmacao.fazer_nada()#chama uma função do organismo/obj_avatar
                        
                elif opcao == 6:
                        print("\n--- Menu de Comidas ---\n")
                        print("1. Carne podre")
                        print("2. Carne Crua")
                        print("3. Carne Assada")
                        
                        escolha = int(input("Escolha o número da sua comida: "))
                        indice = int(input("Informe o índice do avatar que você quer alimentar:"))
                        confirmacao = sistema.avatares[indice]
                        confirmacao.alimentar(escolha)
                        
                elif opcao == 7:
                        print("\n--- Menu de Hidratação ---\n")
                        print("1. Água Potável")
                        print("2. Água de coco")
                        print("3. Água suja")
                                
                        escolha = int(input("Escolha o número da sua hidratação:"))
                        indice = int(input("Informe o índice do avatar que você quer hidratar:"))
                        confirmacao = sistema.avatares[indice]
                        confirmacao.hidratar(escolha)
                        
                elif opcao == 8:
                        print("\n--- Menu de Proteção para a Pele ---\n")
                        print("1. Protetor Solar")
                        print("2. Repelente")
                        print("3. Blusa de frio")
                                
                        escolha = int(input("Escolha o número da sua proteção:"))
                        indice = int(input("Informe o índice do avatar que você quer proteger:"))
                        confirmacao = sistema.avatares[indice]
                        confirmacao.proteger(escolha)
                        
                elif opcao == 9:
                        indice = int(input("Informe o índice do avatar que você quer movimentar:"))
                        distancia = float(input("Informe a distância que você deseja movimentar o seu avatar:"))
                        confirmacao = sistema.avatares[indice]
                        confirmacao.movimentar(distancia)
                        
                elif opcao == 10:
                        print("Ok, volte sempre!")
                                break
                        
                else:
                                print("Opção inválida!")
                        
        elif play == 'n':
                resposta = ("Deseja sair? s/n")
                       if resposta == 's':
                                print("Ok, volte sempre!")
                                break
                       elif resposta == 'n':
                               pass
                               #como faz pra voltar???       
        else:
                print("Opção inválida!")



###FALTA CRIAR NO MAIN:
#mÉTODOS DO ÚTERO 
#MÉTODOS DA PELE




#organismo

from Pele import Pele
from Utero import Utero
from random import choice
from Bioma import Bioma
from FlorestaTrop import FlorestaTropical
from Savana import Savana
from Tundra import Tundra

class Organismo():
    def __init__(self, nome, idade, peso, bioma):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.energia = 100
        self.intensidade_dor = 0
        self.bioma = Bioma()
        self.pele = Pele (melanina = random.choice(["baixa", "média", "alta"])) #####será que mostra a cor da pele pro usuário??
        self.utero = Utero()
        self.fome = 0


    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        if self.peso >= 70:
            quilos_extras = self.peso - 70
            gasto += gasto * (quilos_extras * 0.01)
        self.energia -= int(gasto)
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")


    def hidratar(self, escolha):
        if escolha == 1:
            self.energia += 10
            print(f"Parabéns, {self.nome}! Você bebeu 200ml de água potável!") 

        elif escolha == 2:
            self.energia += 15 
            print(f"Maravilha! {self.nome} Você bebeu 200ml de água de coco!") 

        elif escolha == 3:
            self.energia -= 15
            print(f"Que nojo! {self.nome} você bebeu 200ml de água suja!") 

        else:
            print("Opção inválida! Você não bebeu nada.")
            self.energia -= 10


    def alimentar(self, escolha):
        if escolha == 1:
            self.energia -= 15
            self.fome += 5 
            print(f"Ops! {self.nome} tinha opção melhor hein.")

        elif escolha == 2:
            self.energia += 5
            self.fome -= 5
            print("Foi quase hein! Boa sorte na próxima.")

        elif escolha == 3:
            self.energia += 15
            self.fome -= 10
            print("Opção incrível!! Parabéns") 

        else:
            print("Opção inválida! Você não comeu nada.")
            self.fome += 15
            self.energia -= 15 
    
        
    def fazer_nada(self):
        if self.energia >=10 :
            self.energia -= 10
            print(f"Deu mole, perdeu energia. Energia atual {self.energia}")

        elif (self.energia == 0) and (self.fome == 100):
            print(f"Você está sem energia e com muita fome. {self.nome} não sobreviveu.")

        elif (self.energia == 0) and (self.fome <= 60):
            print(f"Você está sem energia e com fome. {self.nome} melhor comer e se hidratar.")
            

    def proteger(self, escolha):
        if escolha == 1: #protetor solar
            if isinstance(self.bioma, Savana):
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você usou o protetor solar e protegeu a pele na Savana!")

            elif isinstance(self.bioma, FlorestaTropical): 
                self.intensidade_dor += 1
                print("Você usou o item errado! Muitas picadas de mosquito na Floresta Tropical aumentaram sua dor.")

            elif isinstance(self.bioma, Tundra): 
                self.intensidade_dor += 1
                print("Você usou o item errado! O frio da Tundra aumentou sua dor.")

        elif escolha == 2: #repelente
            if isinstance(self.bioma, FlorestaTropical): 
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você usou o repelente e afastou os insetos da Floresta Tropical!")

            elif isinstance(self.bioma, Savana): #is instance????
                self.intensidade_dor += 1
                print("Você usou o item errado! O sol da Savana aumentou sua dor.")

            elif isinstance(self.bioma, Tundra):
                self.intensidade_dor += 1
                print("Você usou o item errado! O frio da Tundra aumentou sua dor.")

        elif escolha == 3: #blusa de frio
            if isinstance(self.bioma, Tundra): 
                self.intensidade_dor = max(0, self.intensidade_dor - 1)
                print("Parabéns, você vestiu a blusa de frio e se aqueceu na Tundra!")

            elif isinstance(self.bioma, FlorestaTropical): 
                self.intensidade_dor += 1
                print("Você usou o item errado! Muitas picadas de mosquito na Floresta Tropical aumentaram sua dor.")# não faz sentido, eu acho, pq a blusa ajuda um pouco

            if isinstance(self.bioma, Savana):
                self.intensidade_dor += 1
                print("Você usou o item errado! O calor escaldante da Savana aumentou sua dor.")

        else:
            print("Opção inválida! Você não se protegeu.")
            self.intensidade_dor += 3
            
            
from Organismo import Organismo
import random 

class Utero():
    def __init__(self):
        self.tamanho_utero = 10

    def __init__(self, organismo, tamanho_utero = 10, saude =  10):
        self.organismo = organismo
        self.tamanho_utero = self.tamanho_utero
        self.saude = self.saude

    def atualizar_tamanho_por_idade(self, idade):#a idade não está sendo acessada
        if self.organismo.idade < 12:
            self.tamanho_utero = 5  
        elif self.organismo.idade > 55:
            self.tamanho_utero = 7  
        else:
            self.tamanho_utero = 10 

    def menstruar(self):
        if self.organismo.idade >= 12 and self.organismo.idade <= 55:
            
            if self.organismo.fome >= 60 or self.organismo.energia <= 40:
                self.saude -= 2
                print("Cuidado! você tem um índice de saúde baixo.")
                
            else:
                self.saude = self.saude
                print("Você está menstruando normalmente!")
                
        else:
            self.saude = 10
            print("Você não está na idade fértil.")

    def verificar_status(self):
        print("--- Status do Útero ---")
        print(f"Tamanho do útero: {self.tamanho_utero}")
        print(f"Saúde do útero: {self.saude}")

        if self.saude <= 4:
            print("Estado crítico!")
        elif self.saude <= 7:
            print("Estado de atenção.")
        else:
            print("Estado saudável.")
        
        idade = self.organismo.idade
        if idade < 12:
            print("Você ainda não passou pela menarca garotinha!")
        elif idade > 55:
            print("Você está na fase pós-menopausa")
        else:
            print("Que útero abençoado! Está super fértil")
            
            
            
from Organismo import Organismo
import random 

class Pele():
    def __init__(self, melanina):
        self.melanina = melanina
        self.verificar_protecao = False
 
    def tomar_sol(self):
        if self.melanina == "baixa":
            print("Você está tomando sol, mas sua pele é sensível. Cuidado com queimaduras!")
            self.verificar_protecao = True
        elif self.melanina == "media":
            print("Você está tomando sol, sua pele tem proteção moderada.")
            self.verificar_protecao = True
        elif self.melanina == "alta":
            print("Você está tomando sol, sua pele tem alta proteção natural.")
            self.verificar_protecao = True
    

    def tomar_sol(self, tem_protetor_solar=False):######vai ficar com qual????#até então usei esse
        print("Você está na Savana tomando sol...")#funciona nos outros biomas tbmm ou não??
        if self.melanina == "baixa":
            if tem_protetor_solar == True:#esse é muito bom só teria q atualizar essa variável tbm
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.verificar_protecao = True
                
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.verificar_protecao = False

        elif self.melanina == "média":
            if tem_protetor_solar == True:###
                print("✨ Com protetor solar, sua pele está super protegida!")
                self.verificar_protecao = True
            else:
                print("Você tem proteção moderada, mas o sol da Savana é forte. Cuidado com o tempo de exposição.")
                self.verificar_protecao = True 

        elif self.melanina == "alta":
            print("✨ Sua pele tem alta proteção natural contra os raios da Savana!")
            self.verificar_protecao = True