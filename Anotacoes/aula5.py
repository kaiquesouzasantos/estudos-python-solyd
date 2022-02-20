# ===================== coleções =====================
lista = ['Kaique','João'] # LISTA(list)/array => permite manipulação de length
tupla = ('Kaique','João') # TUPLA(tuple) => não permite alteração de length
dicionario = {'nome':'Kaique','idade':15} # DICIONARIO(dict) => (semelhante ao objeto) permite manipulação de length # 'palavra' :(=) 'significado'
conjunto = {'Kaique','João'} # CONJUNTO(set) => não aceita itens iguais, não tem indice, permite manipulação de length

lista1 = []
tupla1 = ()
dicionario1 = {} # dicionario1 = dict()
conjunto1 = set()

for nome in tupla: # percorre a coleção
    print(nome)

if 'Kaique' in tupla: # consulta elemento dentro da coleção
    print('Kaique está na tupla')

print(dicionario['nome']) # consulta elemento sem o indice

print(len(dicionario))

for valores in dicionario:
    print(valores)

if 'Kaique' in dicionario.values(): # values => referencia as chaves
    print('Kaique está no dicionario!')

if 'Kaique' in dicionario.keys(): # semelhante ao VALUES
    print('Kaique está no dicionario!')

dicionario['nome'] = 'João'
dicionario['idade'] = 100
dicionario['endereço'] = 'Av. Jonas Martins' # adicona elemento no dict
# dicionario.clear() => limpa
print(dicionario)

conjunto.add('Maria') # adiciona elemento no set
conjunto.add('Kaique') # não adiciona, pois já tem um elemento igual dentro do set
if 'Kaique' in conjunto: # possui uma busca rápida
    print('foi encontrado dentro do conjunto')
print(conjunto)

# CONJUNTO é algo não relacional, não possui indice = velocidade de pesquisa superior em larga escala | ARRAY(list) faz a leitura de acordo com o indice

loucura = [(1,2),(3,4),(5,6),({'João','Maria'},{'Kaique'})] # lista que tem tuplas, onde uma tupla tem dois conjuntos, onde um conjunto possui 2 itens
print(loucura)