from datetime import date,time,datetime
import time

def teste():
    print("Digite a Data Para o Inicio da Votação. Exemplo <01/01/2001>")
    data_inicial_do_pleto = str(input())

    print("Digite a Hora. Exemplo um numero de <00 a 23>")
    horaI = time.hour = str(input())
    print("Digite os Minutos. Exemplo um numero de <00 a 59>")
    minutosI = time.minute = str(input())
    segundos = time.second = str(00)
    hora_inicial =  " " + horaI + minutosI
    data_inicial_do_pleto  += hora_inicial + segundos

    data_inicial = datetime.strptime(data_inicial_do_pleto, '%d/%m/%Y %H%M%S')#data inicial do pleto
    print("Digite a Data Para a Finalização do Votação. Exemplo <01/01/2001>")
    data_final_do_pleto = str(input())
    print("Digite a Hora. Exemplo um numero de <00 a 23>")
    horaF = time.hour = str(input())
    print("Digite os Minutos. Exemplo um numero de <00 a 59>")
    minutosF = time.minute = str(input())

    hora_final = " " + horaF + minutosI
    data_final_do_pleto += hora_final + segundos
    data_final = datetime.strptime(data_final_do_pleto, '%d/%m/%Y %H%M%S')#data final do pleto
    if data_final < datetime.today():
        print("A data de finalização da votação deve ser maior ou igual a data de hoje.")
        loop = True
    elif data_inicial > data_final:
        print("A data de inicio da votação esta maior do que a data de finalização.\nPor favor corrija")
        loop = True
    else:
        data_inicial = data_inicial.strftime('%d/%m/%Y %H:%M:%S')
        data_final = data_final.strftime('%d/%m/%Y %H:%M:%S')
        print("A data De inicio da votação sera: {}\nE a data de finalização da votação sera: {}".format(data_inicial, data_final))
        loop = False
