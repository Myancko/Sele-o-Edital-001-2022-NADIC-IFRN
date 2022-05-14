from pegar_linha import pegar_linha_txt
from datetime import datetime
import os

"""
olha a data final de um txt esse ela for menor do que a data de Hoje o a votação se encerra"""

def fim_de_votacao (numero_do_txt):
    #print("informe o numero do txt")
    #numero = 6#int(input())
    datai,dataf = pegar_linha_txt(1,numero_do_txt,4)
    data_final = dataf[21:37]

    #print(type(data_final))
    data_final = datetime.strptime(data_final, "%d/%m/%Y %H:%M")
    #print(type(data_final))

    data_agr = datetime.today() #pega a data de agr
    data_agr = data_agr.strftime("%d/%m/%Y %H:%M")
    data_agr = datetime.strptime(data_agr, "%d/%m/%Y %H:%M")
    #print(data_agr)

    if data_final < data_agr:
        print("Essa votação ja expirou me desculpe")
        x = open("codigo back_end/Eleicoes_em_votação/" + str(numero_do_txt) + ".txt", "a", encoding=  'utf-8')
        x.write(" ="*25+"ESSA VOTAÇÃO JA FOI ENCERRADA" + " =")
        x.close()
        x = open("codigo back_end/Eleicoes_em_votação/" + str(numero_do_txt) + ".txt", "r", encoding=  'utf-8')
        a = x.read()
        x.close()
        y = open("codigo back_end/Eleicoes_Concluidas/" + str(numero_do_txt)  + "  Votacao_Expirada.txt", "w", encoding= 'utf-8')  
        y.write(a)
        y.close()
        remove = "codigo back_end/Eleicoes_em_votação/" + str(numero_do_txt) + ".txt"
        os.remove(remove)
        status_da_votacao = False
        return status_da_votacao
    
    print("Votação em andamento")

    status_da_votacao = True
    return status_da_votacao
#fim_de_votacao()