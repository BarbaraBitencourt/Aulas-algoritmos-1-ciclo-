"""

#VÁRIAVEIS GLOBAIS 
PI = 3.1416
variável_global = "PI"


#USO DA VARIÁVEL GLOBAL PI W "várivel_global"
def área_cirucunferência(raio):
    print("uso da variável global ", variável_global,  " = ", PI)
    return PI*pow(raio, 2)

def comprimento_circunferência(diâmetro):
    print("uso da variável global ", variável_global, " = ", PI)
    return PI*diâmetro

print ("A cincunferência de raio 3 tem área = ", área_cirucunferência((3)))
print ("Acincruferência de diâmetro 6 tem comprimento = ", comprimento_circunferência((6)))


"""
"""
#VARIÁVEIS GLOBAIS
PI = 3.1416
print("\n")
def converte_radiano(graus):
    PI = 3.14
    radianos = (graus*PI)/180
    print("o valor da variável local PI = ", PI)
    return radianos

print("90º equivale a ", converte_radiano(90), "radianos")
print("180º equivale a ", converte_radiano(180), "radianos")
print("270º← equivale a ", converte_radiano(270), "radianos")
print("360º equivale a ", converte_radiano(360), "radianos")

print("\nO VALOR GLOBAL DE PI NÃO É ALTERADO PELA FUNÇÃO 'converte_radiano' \ne continua PI = ", PI)

"""
"""

def valida_data(ano_nascimento, mínimo, máximo):
    while True:
        if ano_nascimento < mínimo or ano_nascimento > máximo:
            print(f"crinaça com idade não permitida para a matrícula: ano de nascimento deve ser maior {mínimo} e menor {máximo}")
            return False
        else:
            return True
                    
print("SERVIÇO DE MATRÍCULA NA ESCOLA")
nome = input("Entrar com o nome da criança  ")
mín = int(input("Entre com o ano limite mínimo para matrícula   "))
máx = int(input("Entre com o ano limite máximo para matriculça   "))
ano = int(input("Entre com o ano de nascimento          "))
valida_matricula = valida_data(ano, mín, máx)
if valida_matricula:
    print("A cirança  ", nome, " teve a matrícula efetuada")
else:
    print("A criança ", nome, " não teve a matrícula efetuada porque está fora da idade permitida")


"""    
"""

print("FUNÇÕES COMO PARAMÊTROS DE OUTRAS FUNÇÕES")

def múltiplas_operações(a,b, operação_aritmétrica):
    return operação_aritmétrica(a, b)

def soma(c , d):
    return c + d

def subtração(d, e):
    return d - e

def multiplicação(f, g):
    return f * g

def divisão(h, i):
    return h/i

x = 2.14
y =  -9.33

print(f"operação de soma {x} + {y} = ", múltiplas_operações(x, y, soma))
print(f"operação de subtração {y} - {x} = ", múltiplas_operações(y, x, subtração))
print(f"operação de multiplicação {x} * {y} = ", múltiplas_operações(x, y, multiplicação))
print(f"operação de divisão {x} / {y} = ", múltiplas_operações(x, y, divisão))

"""

