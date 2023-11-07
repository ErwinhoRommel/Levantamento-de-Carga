# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:23:02 2023

@author: Erwin Rommel
"""

import math

def dados(largura, comprimento):
    P = 2*(largura + comprimento)
    A = largura * comprimento
    D = int(input('digite 1 para levantamento de carga e 2 para iluminação:'))
    C = input('qual o comodo? Banheiro, Cozinha, Sala, Quarto ou Outro?' ).lower()
    
    if D == 1:
        if C == ('banheiro'):
            print('1 TUG de 600VA proximo ao lavatorio')
        elif C == ('cozinha'):
            TUG1 = P/(3.5)
            if TUG1 <= 6:
                Pot1 = 3*600 + ((math.ceil(TUG1)+2)-3)*100
            else:
                Pot1 = 2*600 + (math.ceil(TUG1))*100
            print('O numero de TUGs vai ser: ')
            print(math.ceil(TUG1)+2)
            print('De potencia: ')
            print(Pot1,'VA')
        elif C == ('sala'):
            TUG2 = P/5.0
            Pot2 = math.ceil(TUG2)*100
            print('O numero de TUGs vai ser: ')
            print(math.ceil(TUG2))
            print('De potencia: ')
            print(Pot2,'VA')
        elif C == ('quarto'):
            TUG3 = P/5.0
            Pot3 = math.ceil(TUG3)*100
            print('O numero de TUGs vai ser: ')
            print(math.ceil(TUG3))
            print('De potencia: ')
            print(Pot3,'VA')
        elif ((C == 'outro') and (A < 6.0)):
            print('1 TUG de 100VA')
        elif ((C == 'outro') and (A >= 6.0)):
            TUG = P/5.0
            Pot4 = math.ceil(TUG)*100
            print('O numero de TUGs vai ser: ')
            print(math.ceil(TUG))
            print('De potencia: ')
            print(Pot4,'VA')
        else:
            print('este caso não esta disponivel no sistema')
    if D == 2:
        if A <= 6:
            print('1 ponto de 100 VA')
        else:
            if A % 4 == 0:
                ilum = (A/4) + 1
                Poti = (A/4)*60 + 100
                print(ilum,'pontos de',Poti,'VA')
            else:
                ilum = int((A/4) + 1)
                Poti = int((A/4)*60 + 100)
                print(ilum,'pontos de',Poti,'VA')




if __name__ == '__main__': 
  while prog == True:
    print('levantamento de carga\n')
    largura = float(input('entre com o valor da largura: '))
    comprimento = float(input('entre com o valor do comprimento: '))
    dados(largura, comprimento)
    a = input('o usuario deseja continuar a usar o programa se não tecle q se sim tecle qualquer outra tecla:')
    if  a == 'q':
        prog = False
    