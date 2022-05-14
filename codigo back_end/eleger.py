import os
import time
from unittest import skip
from pegar_linha import pegar_linha_txt
from computar_votos import total_de_votos
from cpf_certo import verificar_cpf
from repeticoes_cpf import verificar_cpf_existencia
from fechar_votação import fim_de_votacao
"""
Esse .py contem 2 metodos um contem o menu de votacao e o outro faz a votação.
A contagem dos votos fica com o arquivo computar_votos.py
"""
def aplicar_voto(numero_do_candidato, numero_do_txt, numero_de_candidatos, cpf):
    validacao = verificar_cpf_existencia(numero_do_candidato, numero_do_txt, numero_de_candidatos, cpf)
    if validacao == True:
        """nos txts de 'eleiçoes em votacao' os candidatos começao a aparecer depois da linha 6"""
        numero_do_txt = str(numero_do_txt)
        x = open("codigo back_end/Eleicoes_em_votação/" + numero_do_txt + ".txt", "r+", encoding= 'utf-8')

        candidato_votado = str()
        loop = x.readlines()
        #contador = int(1)
        if numero_do_candidato > numero_de_candidatos:
            print("erro, o numero do candidato nao pode ser maior do que o numero do candidato")
            time.sleep(0.5)
            return "Erro ao executar a votação Por favor tente novamente."
        candidato_votado  +=  loop[5 + numero_do_candidato] #+ "+1 voto"
        l = len(candidato_votado)
        candidato_votado  =  candidato_votado[0:l - 1]
        candidato_votado += "  +1 voto"

        y = open("codigo back_end/Eleicoes_em_votação/" + numero_do_txt + ".txt", "a+", encoding= 'utf-8')
        y.write("\n" + cpf + "\n" + candidato_votado +"\n")
        y.close()
        return candidato_votado
    else:
        print("=" *  36)
        print("<<< Digite enter para continuar >>>")
        print("=" *  36)
        return input()
def votar():
    os.system("cls")
    time.sleep(0.3)
    
    loop,  cpf_digitado = verificar_cpf()

    while loop == True:
        os.system("cls")
        print("Seu cpf é:", cpf_digitado + "." ,"Digite:")
        print("\n[1] Para votar\n[2] Para obter lista de votações\n[3] Para digitar outro CPF\n[4] Para Voltar")
    
        try:
            seletor = int(input("\n>>> "))
        except:
            seletor = int(-1)
        os.system("cls")
        if seletor == 1:
            print("Digite o numero da votação. ou digite -1 para voltar para o inicio")
            try: 
                numero_da_votação = int(input(">>>  "))
                numero_da_votação = str(numero_da_votação)
                x = open("codigo back_end/Eleicoes_em_votação/" + numero_da_votação + ".txt", "r", encoding=  'utf-8')
                nome_da_eleição = pegar_linha_txt(1,numero_da_votação,1)
                tamanho = len(nome_da_eleição)
                nome_da_eleição = nome_da_eleição[:tamanho - 1]
                fim_de_votacao(numero_da_votação)
                print("Carregando a Votação: {} ".format(nome_da_eleição))
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.5)
                print(".")
                nome_dos_candidatos = pegar_linha_txt(1,numero_da_votação,2)
                print("Carregando lista dos candidatos:")
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.5)
                print(".")
                quantidade_de_candidatos = pegar_linha_txt(1,numero_da_votação,3)
                quantidade_de_candidatos = int(quantidade_de_candidatos)
                print("á {} candidatos Registrados nessa votação.".format(quantidade_de_candidatos))
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.5)
                print(".")
                print(nome_dos_candidatos)
                print("=" *  36)
                print("Voce deseja votar em qual candidato?\n")
                try: 
                    voto = int(input(">>>  "))
                    print(aplicar_voto(voto,numero_da_votação,quantidade_de_candidatos,cpf_digitado))
                    input("<<< Digite enter para continuar >>>\n")
                    #total_de_votos(voto,numero_da_votação)
                except:
                    print("Ocorreu um erro na digitação do voto, pro favor tente novamento")
                    print("Voltando")
                    time.sleep(0.2)
                    print(".")
                    time.sleep(0.2)
                    print(".")
                    time.sleep(0.5)
                    input("Digite enter")
                    os.system("cls")

            except:
                print("Erro, verifique se a votacões em andamento")
                numero_da_votação = 0

            if numero_da_votação == -1:
                print("Voltando")
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.5)
                os.system("cls")
            elif  numero_da_votação == 0:
                print("Numero invalido")
                print("Voltando")
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.5)
                os.system("cls")

                

        elif seletor == 2:
            
            try:
                x = open("codigo back_end/Eleicoes_em_votação/total_de_pletos.txt",  "r")
                total_de_pleitos = x.readline()
                contador = int(1)
                total_de_pleitos = int(total_de_pleitos)
                print("Total de pleitos Registrados no Sistema =", total_de_pleitos , "\n", "-" * 50 )
                while contador <= total_de_pleitos:
                    contador = str(contador)
                    votacao = open ("codigo back_end/Eleicoes_em_votação/"  + contador  + ".txt", "r", encoding=  'utf-8')
                    vota = votacao.read()
                    vota = vota[2:]
                    print("{}".format(vota))
                    contador = int(contador) 
                    contador += 1
                    print("-" * 51 )
                    input("<<< Digite enter para continuar >>>\n")
            except:
                print("não a nem um pleito em andamento por favor crie um")
                input("\n<Digite enter para continuar>\n>>>  ")
        
        elif  seletor == 3:
            
                loop, cpf_digitado = verificar_cpf()
        elif seletor == 4:
            return 0
        else:
            print("valor invalido.")
#votar()