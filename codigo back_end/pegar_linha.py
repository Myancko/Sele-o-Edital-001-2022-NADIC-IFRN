"""Esse txt contem a função que retorna uma linha de um txt
a variavem 'um_ou_dois' se refere a pasta em que a busca sera feita 
1 para eleicoes_em_votação, 2 para informaçoes_dos_candidatos 

variavel 'o_que_pegar'

1 = nome da votação
2 = nome dos candidatos
3 = quantidade de candidatos
4 = data de inicio e fim da votação

"""

def pegar_linha_txt (um_ou_dois = 1, numero_do_txt = 4,  o_que_pegar = 4):
    contador = int(0)
    if um_ou_dois ==  1:
        um_ou_dois = "Eleicoes_em_votação"
        #print("o que voce deseja retornar.Digite")
        #print("[1] nome da votação\n[2] nome dos candidatos\n[3] quantidade de candidatos\n[4] pegar data ")
        #seletor = int(input())
        seletor = int(o_que_pegar)
        if seletor == 1:
            numero_do_txt = str(numero_do_txt)
            x = open("codigo back_end/" + um_ou_dois + "/" + numero_do_txt + ".txt", "r", encoding=  'utf-8')
            x.readline()
            texto = x.readline()
            #print(texto[17:])
            #input() 
            return texto[17:]

        elif seletor == 2:
            numero_do_txt = str(numero_do_txt)
            x = open("codigo back_end/" + um_ou_dois + "/" + numero_do_txt + ".txt", "r", encoding=  'utf-8')
            x.readline()
            x.readline()
            x.readline()
            x.readline()
            total_de_candidatos = x.readline()
            total_de_candidatos = total_de_candidatos[26:]
            total_de_candidatos = int(total_de_candidatos)
            contador = int(1)
            candidatos= x.readlines()
            #print(candidatos)
            #input("x")
            lista_candidatos = str()
            while contador <= total_de_candidatos:
                #print(candidatos[contador])
                lista_candidatos +=  str(candidatos[contador])  + "\n"
                contador += 1
            return lista_candidatos
        elif seletor == 3:
            numero_do_txt = str(numero_do_txt)
            x = open("codigo back_end/" + um_ou_dois + "/" + numero_do_txt + ".txt", "r", encoding=  'utf-8')
            x.readline()
            x.readline()
            x.readline()
            x.readline()
            quantidade_de_candidatos = x.readline()
            quantidade_de_candidatos = quantidade_de_candidatos[26:]
            return quantidade_de_candidatos
        elif seletor == 4:
            numero_do_txt = str(numero_do_txt)
            x = open("codigo back_end/" + um_ou_dois + "/" + numero_do_txt + ".txt", "r", encoding=  'utf-8')
            x.readline()
            x.readline()
            data_inicio = x.readline()
            data_fim  = x.readline()
            #print(data_inicio, data_fim)
            return data_inicio, data_fim

"""n vi nescessidade de continuar, caso eu precise usar essas informaçoes eu volto aqui
e programo essa parte"""
            
#    elif um_ou_dois == 2:
#        um_ou_dois = "Informaçoes_dos_candidatos"
#        
#    numero_do_txt = str(numero_do_txt)
#    #numero_da_linha = str(numero_da_linha)
#    while contador < numero_da_linha:
#
#        x = open("codigo back_end/" + um_ou_dois + "/" + numero_do_txt + ".txt", "r", encoding=  'utf-8')
#        x.readline()
#        print(x.readline())
#        input()
#pegar_linha_txt()