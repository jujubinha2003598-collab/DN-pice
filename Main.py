import random
from Bioma import Bioma
from FlorestaTrop import FlorestaTropical
from Savana import Savana
from Tundra import Tundra
from Organismo import Organismo
from Pele import Pele 
from Utero import Utero


        print("\n--- Biomas ---\n")
        print("1. Floresta Tropical")
        print("2. Savana")
        print("3. Tundra")
        
        escolha = input("Escolha o bioma:")
        obj_organismo.proteger(escolha)

        print("\n--- Menu de Comidas ---\n")
        print("1. Carne podre")
        print("2. Carne Crua")
        print("3. Carne Assada")
        
        escolha = input("Escolha a comida: ")
        obj_organismo.alimentar(escolha)


        print("\n--- Menu de Proteção para a Pele ---\n")
        print("1. Protetor Solar")
        print("2. Repelente")
        print("3. Blusa de frio")
        
        escolha = input("Escolha a proteção:")
        obj_organismo.proteger(escolha)

        print("\n--- Menu de Hidratação ---\n")
        print("1. Água Potável")
        print("2. Água de coco")
        print("3. Água suja")
        
        escolha = input("Escolha a hidratação:")
        obj_organismo.hidratar(escolha)






