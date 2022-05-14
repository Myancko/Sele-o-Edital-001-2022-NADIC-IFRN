"""Esse .py faz parte do sistema de eleiçoes, ele cria eleiçoes e as armazena em um txt
para que mais tarde elas possam ser acessadas"""

"""
Eleição: 
1 deverá informar o nome do pleito, 
2 data inicial e final do pleito, 
3 a quantidade de candidatos e quem serão os candidatos.
para isso, é necessário também realizar o cadastro do candidato;  >>> sera feito em outro .py

"""

from datetime import datetime, date, time
import os
from unittest import skip
import time
print(datetime.today())
os.system("cls")

#class pleto:
#    def __init__ (self, nome, dataI, dataF, quantidade_de_cadidatos, descricao):
#        self.nome = nome
#        self.dataI = dataI
#        self.dataF = dataF
#        self.quantidade

def criar_pleito ():

    print("Digite o nome para o Pleito")
    nome_do_pleto = str(input("\n>>> "))#nome do pleto
    os.system("cls")
    big_one = True

    while big_one == True:
        loop2 = True
        while loop2 == True:
            print("Digite a Data Para o Inicio da Votação. Exemplo <01/01/2001>")
            try:
                data_inicial_do_pleto = str(input("\n>>> "))
                loop2 = False
            except:
                print("Erro na data digitada, lembre de usar 01 ao em vez de só 1")
        loop2 = True
        while loop2 == True: 
            print("Digite a Hora. Exemplo um numero de <00 a 23>")
            try:
                horaI = time.hour = str(input("\n>>> "))
                loop2 = False
            except:
                print("Erro no numero Digitado")   
        loop2 = True
        while loop2 == True: 
            print("Digite os Minutos. Exemplo um numero de <00 a 59>")
            try:
                minutosI = time.minute = str(input("\n>>> "))
                loop2 = False
            except:
                print("Erro no numero Digitado")
        try:
            hora_inicial =  " " + horaI + minutosI
            data_inicial_do_pleto  += hora_inicial 
            data_inicial = datetime.strptime(data_inicial_do_pleto, '%d/%m/%Y %H%M')#data inicial do pleto
            big_one = False
        except:
            os.system("cls")
            print("Houve um erro na digitação da data ou das horas. Por favor tente novamente.\n")
            big_one = True
    big_one = True
    os.system("cls")
    while  big_one == True:
        print("Digite a Data Para a Finalização do Votação. Exemplo <01/01/2001>")
        loop2 = True
        while loop2 == True:
            try:
                data_final_do_pleto = str(input("\n>>> "))
                loop2 = False
            except:
                os.system("cls")
                print("Erro na data digitada, lembresse digite a data assim 01/01/2001, não assim 1/1/2002")
        loop2 = True
        while loop2 == True:
            print("Digite a Hora. Exemplo um numero de <00 a 23>")
            try:
                horaF = time.hour = str(input("\n>>> "))
                loop2 = False
            except:
                os.system("cls")
                print("Erro na Hora Digitada")
        loop2 = True
        while loop2 == True:
            print("Digite os Minutos. Exemplo um numero de <00 a 59>")
            try:
                minutosF = time.minute = str(input("\n>>> "))
                loop2 = False
            except:
                os.system("cls")
                print("Erro na Hora Digitada")
        try:
            hora_final = " " + horaF + minutosF
            data_final_do_pleto += hora_final 
            data_final = datetime.strptime(data_final_do_pleto, '%d/%m/%Y %H%M')#data final do pleto
            big_one = False
        except:
            os.system("cls")
            print("Houve um erro na digitação da data ou das horas. Por favor tente novamente.\n")
            loop = True
    if data_final < datetime.today():
        print("A data de finalização da votação deve ser maior ou igual a data de hoje.")
        loop = True
    elif data_inicial > data_final:
        print("A data de inicio da votação esta maior do que a data de finalização.\nPor favor corrija")
        loop = True
    else:
        try:
            data_inicial = data_inicial.strftime('%d/%m/%Y %H:%M')
            data_final = data_final.strftime('%d/%m/%Y %H:%M')
            print("A data De inicio da votação sera: {}\nE a data de finalização da votação sera: {}".format(data_inicial, data_final))
            loop = False
        except:
            os.system("cls")
            print("Houve um erro na digitação da data ou das horas. Por favor tente novamente.\n")
            loop = True
    
    print("\n<<< Digite ENTER para continuar >>>\n")
    input(">>> ")


    os.system("cls")
    loop1 = True
    while loop1 == True:
        print("Digite Quantos Candidatos Participaram da Votação")
        try: 
            quantidade_de_candidatos =  int(input("\n>>> "))#numero total de candidatos a o pleito
        except:
            quantidade_de_candidatos = -1
        print("A quantidade de candidatos que deveram participar nesse plaito é:", quantidade_de_candidatos)

        try:
            total_de_cadidatos_no_sistema = open("codigo back_end/Informaçoes_dos_candidatos/total_de_candidatos.txt")
            tc = total_de_cadidatos_no_sistema.readline()
        except:
            print("Não a candidatos cadastrados no sistema, Por favor cadastre alguns candidatos".upper())
            return 0
        print("Total de Candidatos Registrados no Sistema =",tc)
        tc = int(tc)
        if tc >= quantidade_de_candidatos and quantidade_de_candidatos >=  1:
            loop2 = True
            while loop2 == True:
                #print("Digite 1 para fazer uma votação\nDigite 2 para fazer uma petição")
                print("Voce deseja.\n[1] Adicionar um Cadidato a Votação\n[2] Ver Lista de candidatos")
                try:
                    seletor = int(input("\n>>> "))
                except:
                    seletor = -1
                if seletor == 1:
                    print("A quantidade de candidatos cadastrados no sistema é {}\n\n(cada candidato tem seu numero que pode variar de 1 a 99+\nCaso tenha alguma duvida na pasta 'Informaçoes_dos_candidatos' cada *numero*.txt representa um candidato)\n".format(tc).title())
                    loop_cadastros = 1
                    lista_de_candidatos = []
                    while loop_cadastros <= quantidade_de_candidatos:
                        print("Digite o numero do {} candidato".format(loop_cadastros))
                        try:
                            numero_do_candidato = int(input("\n>>> "))
                            numero_do_candidato = str(numero_do_candidato)
                            x = open ("codigo back_end/Informaçoes_dos_candidatos/" + numero_do_candidato +  ".txt",  "r")
                            x.readline()
                            x.readline()
                            xx = x.readline()
                            texte = len(xx) - 1
                            lista_de_candidatos.append(xx[6:texte])
                            loop_cadastros += 1
                            print(xx)
                        except:
                            os.system("cls")
                            print("Erro de digitacao. Por favor tente novamente.")
                    loop2 =  False
                    loop1 = False
                elif seletor == 2:
                    print("Carregando lista de candidatos")
                    time.sleep(0.2)
                    print(".")
                    time.sleep(0.2)
                    print(".")
                    time.sleep(0.2)
                    print(".")
                    time.sleep(0.2)
                    contador = 1
                    if tc >= 2:
                        print("À um total de {} candidatos no sistema\nCarregando dados".format(tc)) 
                    elif tc == 1:
                        print("A apenas {} candidato, Carregando Dados".format(tc).title())
                    print(".")
                    time.sleep(0.2)
                    print(".")
                    input("<<< Digite enter para continuar >>>")
                    os.system("cls")
                    while contador <= tc:
                        contador = str(contador)
                        c = open ("codigo back_end/Informaçoes_dos_candidatos/" + contador + ".txt", "r", encoding=  'utf-8')
                        x  = c.read()
                        print("candidato {}:\n\n{}".format(contador,  x))
                        print("\n\n")
                        time.sleep(0.5)
                        contador = int(contador)
                        contador += 1
                        input("<<< Digite enter para continuar >>>")
                elif  seletor == -1:
                    print("valor invalido")

        elif tc <= 0:
            print("A 0 candidatos registrados no sistema por favor, registre alguns cadidatos para que a eleição possa acontecer\nVoce sera redirecionado para o menu inicial")
            input("<<< Digite enter para continuar >>>\n")
            os.system("cls")
            return "Erro não tem nem um Cadidato cadastrado no sistema."

        elif quantidade_de_candidatos <= 0:
            print("A quantidade de candidatos deve ser maior ou igual a 1.")
            input("<<< Digite enter para continuar >>>\n")
        
        elif quantidade_de_candidatos > tc:
            print("A quantidade de cadidatos não pode ser maior do que a quantidade de candidatos cadastrados no sistema = {}\nPor favor cadastre mais candidatos ou escolha um numero menor ou igual a {}".  format(tc, tc))
            input("<<< tecle enter para continuar >>>\n")
            os.system("cls")

    print("Digite uma descrição sobre a votação")
    """descriçao das pessoas que iram votar exemplo, alunos, trabalhadores, politicos etc"""
    try:
        descricao_do_pleto = str(input("\n>>> "))
    except:
        descricao_do_pleto = str("A descrição foi corrompida durante o salvamento, tchitchi")

    contador__de_pleitos = str(1)
    contador = str()
    #stop = int(0)
    loop = True
    while loop == True:
        #if stop == 5:
            #break

        os.system("cls")
        try: 
            pleto = open ("codigo back_end/eleicoes_em_votação/" + contador__de_pleitos + ".txt", "r",encoding=  'utf-8')
            funfa = pleto.readline(1)
        except:
            pleto = open ("codigo back_end/eleicoes_em_votação/" + contador__de_pleitos + ".txt", "w", encoding=  'utf-8')
            pleto.write("não")
            pleto = open ("codigo back_end/eleicoes_em_votação/" + contador__de_pleitos + ".txt", "r", encoding=  'utf-8')
            funfa = pleto.readline(1)

        #print('funfa = ', funfa)
        if funfa == "s":
            contador__de_pleitos = int(contador__de_pleitos) + 1
            contador__de_pleitos = str(contador__de_pleitos)
        else:
            pleto = open ("codigo back_end/eleicoes_em_votação/" + contador__de_pleitos + ".txt", "w", encoding=  'utf-8')
            pleto.write("s Votacao {}\nNome da Votacao: {}\nData de Inicio: {}\nData de Finalizacao: {}\nQuantidade de candidatos: {}\nDescricao da Votação: {}".format(contador__de_pleitos, nome_do_pleto, data_inicial, data_final, quantidade_de_candidatos, descricao_do_pleto ))
            contador = 0
            ordem_de_candidatos = 0
            for canditatos in lista_de_candidatos:
                pleto.write("\nCanditado {} = {}".format(ordem_de_candidatos + 1, lista_de_candidatos[contador]))
                contador += 1
                ordem_de_candidatos += 1
            pleto.write("\n\nNumero de CPF cadastrados:\n")
            pleto.close()

            total_de_votacoes = open ("codigo back_end/eleicoes_em_votação/total_de_pletos.txt", "w", encoding=  'utf-8')
            total_de_votacoes.write("{}\nEsse txt armazena o total de votacoes no sistema para fins de usar em um loop.\nCaso alguma votação seja deletada esse txt estara incorreto e sera atualizado quando a proxima votação for criada.".format(contador__de_pleitos))
            total_de_votacoes.close()
            loop = False
        #stop = stop + 1
    print("Sua pleto foi registrado no sistema")
    #print(pleto.read())
#criar_pleito()