# ===================== tratamento de erros e exeções =====================

try: # try => tentar
    a = 1200 / 0
    print(a)
except: # except => se der errado(exceção) o try
    print('Divisão impossivel')

try: 
    a = 1200 / 0
    print(a)
except ZeroDivisionError: # ZeroDivisionError => erro especifico, atende somente ao mesmo
    print('Divisão impossivel')
except NameError: # NameError => se não atender ao ZeroDivisionError, esse ira suprir 
    print('voce digitou alguma coisa errada')
except Exception as erro: # Exception = except => qualquer exceção # as => atribui o tipo de erro a uma variavel
    print('exceção generica',erro)

def abre_arquivo():
    try:
        arquivo = open('arquivo.txt')
        print('abriu')
        return arquivo
    except:
        print('deu pau!')
        return False
while not abre_arquivo():
    print('tentando abrir o arquivo')


































