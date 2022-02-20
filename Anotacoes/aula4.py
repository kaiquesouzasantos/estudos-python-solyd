# ===================== laços =====================
nomes = ['Kaique','Karina','Joao','Julia']
for nome in nomes: # for(para) [nome] dentro(in) de [nomes] =  percorre os itens dentro da coleção
    print(nome)
for itemN in range(4):
    print(nomes[itemN])
for itemN2 in range(len(nomes)):
    print(nomes[itemN2])
    nomes.append('Oi')
print(nomes)

palavra = 'Kaique Souza Santos'
for letra in palavra:
    print(letra)

lista = range(5) # range() => cria lista 
lista2 = range(5,10) # ponto inicial e final [5<10]
lista3 = range(0,100,2) # step, intervalo [0<100]
for item in lista:
    print(item)

i = 0
while i<=10:
    print('I é menor que 10! | ',i)
    i += 1
print('|    Acabou o laço chefia!   |')

b=0
while b<20 and b<10:
    print('Atende á condição! | ',b)
    b +=1

num = 0

while True:
    print(num)
    if num == 20:
        break
    num += 1
print('Saiu do WHILE!')