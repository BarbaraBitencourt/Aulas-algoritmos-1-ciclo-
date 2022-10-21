# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:29:26 2022

@author: lab54
"""
"""
notas = [0.0, 0.0, 0.0, 0.0, 0.0]
nota_escolhida = 0
i = 0
while i < 5:
    notas[i] = float(input(f"entrar com o valor da nota {i + 1}: \t "))
    i += 1
nota_escolhida  = int (input ("Qual a nota que deseja ver? = "))
print(f"nota escolhida foi a: {nota_escolhida:}ª ")
print("nota = ", notas[nota_escolhida - 1])
                   
"""
"""
#segmentação (fatiamento) de listas
lista_2 = [1, 2, 3, 4, 5,5, 6]
#[a:b] à esquerda dois pontos: posição do início do segmento; à direita dos pontos = posição final
print("\n\nlista_2[0:6] = lista completa ", lista_2[0:6])
print("lista_2[:6] = lista completa ", lista_2[:6])
print("lisra_2[:1] = menos um elemento a partir do fim da lista ", lista_2[:-1])
print("lista_2[:-2] = menos dois elementos a partir do fim da lista ", lista_2[:-2])
print("lista_2[:-3] = menos três elementos a partir do fim da lista", lista_2[:-3])
print("lsita_2[:-5] = menos cinco elementos a partir do fim da lista", lista_2[:-5])
print("lista_2[0:1] = um elemtno a partir do primeiro da lista ", lista_2[0:1])
print("lista_2[0:2] = dois elmentos a partir do primeiro da lista ", lista_2[0:2])
print("lista_2 0:3] = três elementos a partir do primeiro da lista ", lista_2[0:3])
print("lista_2[0:5] =  cinco primeiros da lista ", lista_2[0:5]) 
print("lista_2[0:6] = todos os elemtnos da lista ", lista_2[0:6])
print("lista_2[1:3] = entre o segundo e quarto (não inlcuido) elementos da lista", lista_2[1:3])
print("lista_2[1:4] = entre o segundo e quinto (não incluido) elementos da lista ", lista_2[1:4])
print("lista_2[2:5] = entre o terceiro e sexto (não incluído) elementos da lista ", lista_2[2:5])
print("lista_2[3:5] = entre o quarto e sexto (não incluído) elementos da lista ", lista_2[3:5])
print("lista_2[4:5] = quinto elmento da lista ", lista_2[4:5])
print("lista_2[5:6] = quinto elemento da lista ", lista_2[5:6])
print("lista_2[5:7] = sexto elemento da lista ", lista_2[5:7])


"""

"""

frase = ["que optaram", "na estrada.", "por viver", "filme", "Nomadland", "que conta", "de pessoas", "a história", "é um"]
print("\n\n A frase ordenada é:   ", frase[4:5], "  ", frase[8:9],  "  ", frase[3:4],  " ", frase [5:6], "  ", frase[7:8], " ", frase[6:7], " ", frase[0:1], " ", frase[2:3], " ", frase[1:2])

"""
