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
                        confirmacao.proteger(confirmacao, escolha)
                        
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
                print("Ok, volte sempre!")
                break     
        else:
                print("Opção inválida!")



###FALTA CRIAR NO MAIN:
#mÉTODOS DO ÚTERO 
#MÉTODOS DA PELE