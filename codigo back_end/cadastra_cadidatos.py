"""para isso, é necessário também realizar o cadastro do candidato;  

Candidato: deverá informar o CPF, nome completo, data de nascimento e endereço.
"""
from datetime import datetime
from cpf_certo import verificar_cpf
import time
import os
def Cadastrar_Candidato ():
    os.system("cls")
    print("Cadastrando candidato")
    time.sleep(1)
    print("Digite o Nome Completo.")
    nome = str(input(">>> "))
    if len(nome) <= 1 :
        nome = 'anonimo'
        nome = nome.upper()
    else:
        nome = nome.upper()

    a, cpf = verificar_cpf()

    print("Esse é o CPF", cpf)
    loop = True
    while loop == True:
        try:
            print("Digite a Data de Nascimento. Exemplo 01/01/2001")
            data_nascimento_str = str(input(">>> "))
            data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
            data_nascimento = data_nascimento.strftime('%d/%m/%Y')
            loop = False
        except:
            os.system("cls")
            print("Erro na digitação.\nDigite novamente.\n")
            loop = True


    print("Digite o Endereço. Exemplo Rio de Janeiro, Morro do Dende")
    endereco = str(input(">>> "))
    endereco  = endereco.title()
    loop = True
    contador = str(1)

    print("Digite uma descrição sobre o Candidato")
    descricao = str(input(">>> "))
    while loop == True:

        try: 
            pessoa = open ('codigo back_end/Informaçoes_dos_candidatos/'+ contador + '.txt', 'r', encoding=  'utf-8')
        except:
            pessoa = open ('codigo back_end/Informaçoes_dos_candidatos/'+ contador + '.txt', 'w', encoding=  'utf-8')
        try:
            funfa = pessoa.readline(1)
        except:
            funfa = 'n'
        #print("funfa = ", funfa)

        if funfa == 's':
            contador = int(contador) + 1
            contador = str(contador)
            #print(".", contador)
        else:
            pessoa = open ('codigo back_end/Informaçoes_dos_candidatos/'+ contador + '.txt', 'w', encoding=  'utf-8')
            pessoa.write("sim\nNumero de voto: {}\nNome: {}\nCPF: {}\nData de Nascimento: {}\nEndereço: {}\nDiscrição:  {}".format(contador, nome, cpf, data_nascimento, endereco, descricao))
            pessoa.close()
            totalC = open("codigo back_end/Informaçoes_dos_candidatos/total_de_candidatos.txt", 'w')
            totalC.write("{}\nEsse txt armazena o total de candidatos armazenados no sistema, para fins de usar em um loop".format(contador))
            loop = False
    print("O numero para votar no candidato é", contador,)
    print("O Candidato Foi Cadastrado!!!")

#Cadastrar_Candidato()