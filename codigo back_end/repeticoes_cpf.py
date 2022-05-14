from tracemalloc import stop


def verificar_cpf_existencia(numero_do_candidato= 4, numero_do_txt = 1, numero_de_candidatos=2, cpf = ""):
 
    x = open("codigo back_end/Eleicoes_em_votação/" + str(numero_do_txt) + ".txt", "r+", encoding= 'utf-8')
    a = x.readlines()
    #print(a)
    contador = int(0)
    contador_De_votos= int(0)
    for informacoes in a:
        b = a[contador]
        l = len(b)
        b = b[:l - 1]
        if cpf == b:
            print("O CPF digitado ja foi utilizado na nesta votação.")
            return False
        else:
            #print("não")
            contador +=1
    
    return True


#verificar_cpf_existencia()