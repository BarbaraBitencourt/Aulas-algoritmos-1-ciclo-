# Estruturas-Condicionais-Aninhadas-if-else---elif
Aula 16/09
# -*- coding: utf-8 -*-
"""

@author: Bárbara Bitencourt e Leonardo de Jesus
"""
"""
#TABELA - CÓDIGO PREÇO
#           1     13.30
#           2      1.40
#           3     19.00
#           4     123.49
#           5      44.33

código = int(input("digitar o código do produto\t"))
if código == 1:
    preço_produto = 13.30
elif código == 2:
    preço_produto = 1.40
elif código == 3:
    preço_produto = 19.00
elif código == 4:
    preço_produto = 123.79
elif código == 5:
    preço_produto = 44.33
else:
                    print("\ndigitar código do produto entre 1 e 5: código -> ", código, "não é válido")
                    preço_produto = 0.00
print("\ncódigo do produto =     ", código)
print(f"\npreço do produto de acordo com o código = R$ {preço_produto:4.2f}")

"""
temperatura_ambiente = int(input("digitar a temperatura "))
if temperatura_ambiente >16 and temperatura_ambiente <=30:
    temperatura = "Agradavel"
elif temperatura_ambiente >30:
    temperatura = "Quente"
elif temperatura_ambiente <=16:
    temperatura = "Frio"
else:
    print("valor inválido")
    
print("\nTemperatura = ", temperatura_ambiente, "ºC")
print("\nEntão o clima está ", temperatura)    
    
