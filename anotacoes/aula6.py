# ===================== função =====================
# print() # => função pois tem parenteses ()
# len() # => função
# print(len()) # => função embutida

# função => retorna algo
# metodo => não tem retorno

def soma(num1,num2): # def => define uma função
    resposta = num1 + num2
    return resposta # return => retorna a resposta
retorno = soma(842,1.1)
print(retorno)

def imprimi_oi():
    print('Oi')
i = 1
while i<=10:
    imprimi_oi()
    i+=1

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return ('Sim')
    else:
        return ('Não')
if tem_sete_itens('1234567'):
    print('Tem 7 itens chefia!')