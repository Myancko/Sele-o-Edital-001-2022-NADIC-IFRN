"""
verifica se o cpf digitado contem só numeros, e garante que o CPF digitado tera exatamente 11 Digitos
"""

import time
from unittest import skip
import os
os.system('cls')

def verificar_cpf():
    loop = False
    while loop == False:
        
        print("Para Votar Voce Precisa Digitar o seu CPF\n")

        one = str(input("Digite os 3 primeiros digitos do seu CPF. Exemplo <123.000.000-00>\n>>>  "))
        two  = str(input("Digite os 3 digitos do meio do seu CPF. Exemplo <000.123.000-00>\n\n>>> "))
        three = str(input("Digite os 3 Digitos do CPF quem vem antes do '-'. Exemplo <000.000.123-00>\n\n>>> "))
        four = str(input("Digite os 2 ultimos numeros do seu CPF. Exemplo <000.000.000-12>\n\n>>> "))

        try:
            if int(one) < 0 or int(two) < 0 or int(three) < 0 or int(four) < 0:
                one = "a"
        except:
            skip

        try:
            teste = int(one + two + three + four)
            loop = True
        except:
            time.sleep(0.5)
            print("= "* 25 +"\nErro no CPF, por favor digite um CPF valido.\n" + "= "*25)
            loop = False

        one  = str(one)
        if len(one) < 3:
            x = one
            one = "0" + str(x)
            if len(one) < 3:
                one = "00" + str(x)

        two = str(two)
        if len(two) < 3:
            x = two 
            two = "0" + str(x)
            if len(two) < 3:
                two = "00" + str(x)
        three = str(three)
        if len(three) < 3:
            x = three 
            three = "0" + str(x)
            if len(three) < 3:
                three = "00" + str(x)
        four = str(four)
        if len(four) < 2:
            x = four 
            four = "0" + str(x)

        one  = one[:3]
        two = two[:3]
        three = three[:3]
        four = four[0:2]

        cpf_correto= one + "." + two + "." + three + "-" + four
        print("<<< Digite ENTER para continuar >>>\n")
        input(">>> ")
        os.system("cls")

    return loop, cpf_correto
    """
    o loop retorna como TRUE
    """
#verificar_cpf()