
from pegar_linha import  pegar_linha_txt
from datetime import date, datetime
import locale
import os
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def total_de_votos(numero_do_candidato = 1, numero_do_txt = 4):
    erro = True
    while erro == True:
        print("Digite o numero do txt")
        try: 
            numero_do_txt =  int(input())
            x = open ('codigo back_end/Eleicoes_em_votação/' + str(numero_do_txt) +  ".txt", "r", encoding=  'utf-8')
            a = x.readlines()
            erro = False
        except:
            os.system("cls")
            print("erro no valor digitado.")
            erro = True
    
    total_de_candidatos = pegar_linha_txt( 1, numero_do_candidato, 3)
    contador_loop_contagem = int(1) #é usado para manter o while rodando
    contador_de_votos_dos_candidatos = int(0) # conta os votos de cada candidato e é resetado para 0 no final do loop
    contador_final = int(0) #conta o total de votos de todos os candidatos


    data_agr = datetime.today() #pega a data de agr
    data_agr = data_agr.strftime("%d/%m/%Y %H:%M Dia = %A") #transforma em data normal pra mim

    while contador_loop_contagem <= int(total_de_candidatos):

        numero_do_candidato = contador_loop_contagem
        contador = int(0)
        nome_do_candidato = a[5 +  numero_do_candidato]
        nome_do_candidato = nome_do_candidato[14:]
        nome = nome_do_candidato[:len(nome_do_candidato) - 1] # só o nome
        l = len(nome_do_candidato)
        nome_do_candidato  = nome_do_candidato[0:l - 1]

        n = str(numero_do_candidato)

        voto = ("Canditado "+ str(contador_loop_contagem) + " = " + nome_do_candidato + "  +1 voto\n")
        #print(voto)
        x = open ('codigo back_end/Eleicoes_em_votação/' + str(numero_do_txt) +  ".txt", "r", encoding=  'utf-8')
        a = x.readlines()
        inf = len(a)
        #print(inf)
        #input(".")
        for informacoes in a:
            if voto == a[contador]:
                #print("+1 "  + nome_do_candidato)
                contador_de_votos_dos_candidatos += 1
                contador+=1
                contador_final += 1
            else:
                #print("not")
                contador += 1

        y = open('codigo back_end/Eleicoes_em_votação/' + str(numero_do_txt) +  ".txt", "a", encoding=  'utf-8')
        y.write("\nNumero de votos candidato {} = {}".format(nome, contador_de_votos_dos_candidatos))
        if contador_loop_contagem == int(total_de_candidatos):
            y.write("\nTotal de Votos = {}\nData da Contagem: {}\n".format(contador_final, data_agr))
            y.write("-" * 100)
            y.close()
        else:
            y.close()
        contador_de_votos_dos_candidatos = 0
        contador = int(0)
        contador_loop_contagem += 1

#total_de_votos()