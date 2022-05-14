from criador_de_eleicoes import criar_pleito
from cadastra_cadidatos import Cadastrar_Candidato
from eleger import votar
from computar_votos import total_de_votos
from fechar_votação  import fim_de_votacao
loop = True
while loop == True:

    print("\nVocê Deseja?   (Digite)\n\n[1]Cadastrar Candidatos.\n[2]Criar Votações\n[3]Votar\n[4]Contar os votos de uma eleição\n[5]Sair")#\n[4]Fazer Contagem dos votos)
    try:
        seletor = int(input("\n>>> "))
    except:
        seletor = int(0)

    if seletor == 1:
        Cadastrar_Candidato()

    elif seletor == 2:
        criar_pleito()

    elif seletor == 3:
        votar()

    elif seletor == 4:
        total_de_votos()
        
    elif seletor == 5:
        break

    else: 
        print("O valor digitado esta invalido, Por favor tente novamente")
