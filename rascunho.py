#main

import datetime
from sistema import Sistema
from pessoa import Pessoa
from boletim import Boletim
from turma import Turma
from aluno import Aluno
from professor import Professor

sistema = Sistema()

print("\033[35mBem - Vindo(a) ao Sistema Educacional de Escola de Hangar!\033[m")
while True:
    resposta = input("\033[37mDeseja realizar logins (s/n)?\033[m")
    if resposta == "s" or resposta == "S":
        login = int(input("\033[36mFaça seu login: \n1)Aluno(a): \n2)Professor(a): \n:\033[m")) 
        if login == 1:#criando aluno
            quant_aluno = int(input("Informe a quantidade de alunos que você deseja cadastrar:"))
            for i in range(0, quant_aluno):
                nome = input("Informe o nome do aluno:")

                dia = int(input("Informe a data de nascimento(dd/mm/aaaa) do aluno:\n-Informe o dia:"))
                mes = int(input("-Informe o mês:"))
                ano = int(input("-Informe o ano:"))
                data_na = datetime.date(ano, mes, dia)

                RA_aluno = int(input("Informe seu RA:"))

                senha = input("Crie uma senha:")

                obj_aluno = Aluno(nome, data_na, senha, RA_aluno, 0)
                sistema.cadastrar_aluno(obj_aluno)
                sistema.pessoas.append(obj_aluno)
                print("\033[32mLogin feito com sucesso!\033[m")

        elif login == 2:#criando professor
            quant_prof = int(input("Informe a quantidade de professores que você deseja cadastrar:"))
            for i in range(0, quant_prof):
                nome = input("Informe o nome do professor:")

                dia = int(input("Informe a data de nascimento(dd/mm/aaaa) do professor:\n-Informe o dia:"))
                mes = int(input("-Informe o mês:"))
                ano = int(input("-Informe o ano:"))
                data_na = datetime.date(ano, mes, dia)

                formacao = input("Informe a formação do professor:")

                siape = int(input("Informe o SIAPE do professor:"))

                salario = float(input("Informe o salário do professor:"))

                senha = input("Qual é a senha do professor:")

                obj_prof = Professor(nome, data_na, formacao, siape, salario, senha)
                sistema.cadastrar_professor(obj_prof)
                sistema.pessoas.append(obj_prof)
                print("\033[32mLogin feito com sucesso!\033[m")   

        else:
            print("\033[31mValor inválido!\033[m")
    else:
        #break ou...

        for pessoa in sistema.pessoas:
            pessoa.atuacao() #polimorfismo

        #Criando turmas
        turma = Turma("Turma 1", 1)
        sistema.cadastrar_turma(turma)
        b = 1
        for aluno in sistema.todos_alunos:
            if len(turma.lista_alunos) == 2:
                sistema.todas_turma.append(turma)
                a = len(sistema.todas_turma) + 1
                b = b + 1
                turma = Turma(f"Turma {a}", b)

                turma.lista_aluno.append(obj_aluno)


        if len(turma.lista_alunos) > 0:
            sistema.todas_turma.append(turma)
            
            

        while True:
                confirmacao = input("\033[36mDeseja ir para a sua aba do site? (s/n)\033[m")
                if confirmacao == "s":
                    tipo_usuario = int(input("\033[33mQual é o usuário: \n1)aluno: \n2)professor: \n:\033[m"))

                    if tipo_usuario == 1:
                        print("O que você deseja fazer?")
                        opcao_aluno = int(input("\033[34mOpções para alunos: \n 1)Encontrar a sua turma: \n 2)Ver situação do seu boletim: \n:\033[m"))
                    
                        if opcao_aluno == 1:
                            codigo = int(input("Informe o código da turma que você deseja procurar:"))

                            sistema.buscar_turmas(codigo)

                        elif opcao_aluno == 2:
                            ra = int(input("Informe o RA do aluno:"))

                            sistema.ver_situacao(ra)

                        else:
                            print("\033[31mValor inválido!\033[m")

                    elif tipo_usuario == 2:
                        print("O que você deseja fazer?")
                        opcao_prof = int(input("\033[33mOpções para professores: \n 1)Encontrar a sua turma: \n 2)Ver seus dados: \n 3)Ver alunos: \n4)Dar nota para aluno: \n:\033[m"))

                        if opcao_prof == 1:
                            codigo = int(input("Informe o codigo da turma que você desja procurar:"))

                            sistema.buscar_turmas(codigo)

                        elif opcao_prof == 2:

                            obj_prof.imprimir_dados() 

                        elif opcao_prof == 3:
                            
                            tipo = int(input("Deseja ver: \n1)todos os alunos da sua turma \n2)todos os alunos da escola \n:"))

                            if tipo == 1:
                                codigo = int(input("Informe o código da sala:"))

                                turma.ver_alunos_turma(codigo) # não está funcionando

                            elif tipo == 2:

                                sistema.ver_alunos() 

                            else:
                                print("Valor inválido!")

                        elif opcao_prof == 4:
                            ra = int(input("Informe o RA do aluno:"))
                            valor = float(input("Informe a nota que o aluno tirou:"))

                            sistema.dar_nota(ra, valor) 

                        else:
                            print("\033[31mValor inválido!\033[m")
                elif confirmacao == "n":
                    break
                    
                else:    
                    print("Valor inválido!")








from aluno import Aluno
from professor import Professor
from turma import Turma
from pessoa import Pessoa
from boletim import Boletim


class Sistema():
    def __init__(self):
        self.pessoas = []
        self.todas_turmas = []
        self.todos_alunos = []
        self.todos_professores = []

    def cadastrar_aluno(self, aluno):
        self.todos_alunos.append(aluno)

    def cadastrar_professor(self, Professor):
        self.todos_professores.append(Professor)

    def cadastrar_turma(self, Turma):
        self.todas_turmas.append(Turma)

    def buscar_turmas(self, codigo):#método para encontrar uma turma no sistema
        for turma in self.todas_turmas:
            if turma.codigo == codigo:
                turma.exibir_turma()
            else:
                print("Turma não encontrada!")

    def dar_nota(self, ra, valor):
        for aluno in self.todos_alunos:
            if ra == aluno.RA_aluno:
                aluno.notas = valor 
                print("O professor deu nota", valor, "para o estudante", aluno.nome, "de RA", aluno.RA_aluno,".")
            else:
                print("RA não encontrado")

    def ver_alunos(self):
        for aluno in self.todos_alunos: #todos_alunos
            print("Nome:", aluno.nome, ",", "RA:", aluno.RA_aluno)

    def ver_situacao(self, ra):
        for aluno in self.todos_alunos:
            if ra == aluno.RA_aluno:
                if aluno.notas >= 60 and aluno.notas <= 100:
                    print("Você está aprovado(a) :) com nota:", aluno.notas)
                elif aluno.notas >= 0 and aluno.notas <= 59:
                        print("Essa nota", aluno.notas, "não está no paramêtro de aprovação, logo VOCÊ está reprovado.")
                else:
                    print("\033[31mEssa nota não existe no sistema\033[m")