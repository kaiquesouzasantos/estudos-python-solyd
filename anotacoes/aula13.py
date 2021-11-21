# ===================== Expressões Regulares(regex) =====================

import re # lib para manipulação de arquivos JSON, já vem embutida no python version

string_test = 'O gato é bonito'
padrao = re.search(r'gato',string_test) # search => pesquisa 
# (r'padrão' , 'onde vai ser procurado') 
# # r = converte a string para RAW STRING(string crua,retira os caracteres/especiais)
print(padrao) # retorna o objeto
print(type(padrao)) 
if padrao:
    print(padrao.group()) # retorna o texto
else:
    print('deu pau')

string_test2 = 'gato, gata, gatinhos, gatoes, gat'
padrao2 = re.findall(r'gat\w*',string_test2) # findiall => encontrar/procurar tudo 
# \w => qualquer letra respeitando o limite de 1 caracter = ['gato', 'gata', 'gati', 'gato']
# \w+ => qualquer caracter até finalizar a string agrupada = ['gato', 'gata', 'gatinhos', 'gatoes']
# \w* => retorna tudo = ['gato', 'gata', 'gatinhos', 'gatoes', 'gat']
print(padrao2) # no padrão retorna uma lista
padrao3 = re.findall(r'[gat]',string_test2) # quebra a string e seleciona as correspondentes
padrao4 = re.findall(r'[gat]+',string_test2) # r'[gat]+' => gat ou mais, desde que corresponda á seleção
print(padrao3,padrao4)

# ===================== Expressões Regulares(regex) com emails =====================

teste_e_1 = 'teste@gmail.com'
teste_1 = re.findall(r'\w+@\w+',teste_e_1) 
try:
    teste_1 == True
    print('deu certo',teste_e_1)
except:
    print('deu pau')
    







































