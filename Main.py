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

opcao = int(input("O que deseja fazer? \n1)Criar um avatar \n2)Ver status do avatar \n3)Escolher um bioma \n4)Ver status do bioma \n5)Fazer nada (POR FAVOR, APENAS SE O SEU AVATAR EXISTIR) \n)Sair"))

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
        obj_avatar.fazer_nada()
        
#elif opcao == :#sair
 #       break
        
else:
        print("Opção inválida!")















        print("\n--- Menu de Comidas ---\n")
        print("1. Carne podre")
        print("2. Carne Crua")
        print("3. Carne Assada")
        













        escolha = int(input("Escolha o número da sua comida: "))
        obj_avatar.alimentar(escolha)


        print("\n--- Menu de Proteção para a Pele ---\n")
        print("1. Protetor Solar")
        print("2. Repelente")
        print("3. Blusa de frio")
        
        escolha = int(input("Escolha o número da sua proteção:"))
        obj_avatar.proteger(escolha)

        print("\n--- Menu de Hidratação ---\n")
        print("1. Água Potável")
        print("2. Água de coco")
        print("3. Água suja")
        
        escolha = int(input("Escolha o número da sua hidratação:"))
        obj_avatar.hidratar(escolha)






