# ===================== strings e arrays =====================
frase = 'Oi, tudo bem?' # => lista(array) de caracteres
lista = ['João','Kaique','Maria','Diego']

lista.append('Geraldo') # adiciona elementos no ultimo ligar da lista
lista.remove('João') # remove elementos da lista
lista.insert(1, 'Benjamin') # insert no elemento da lista (sobrescreve)
lista[0] = 'Jonas' # sobrescreve de forma manual
# lista.clear() => limpa a lista 

print(len(lista)) # tamanho da lista
print(len(frase))

print(lista.count('Geraldo')) # conta elementos iguais
print(lista.pop()) # retira o ultimo elemento da lista
print(frase.lower()) # exibe tudo em minusculo
print(frase.upper()) # exibe tudo em maisculo
print(frase.split(',')) # quebra a string utilizando um parametro

print(frase)
print(frase[0])
print(frase[0:5]) # => corte da exibição da lista [0<5]
print(frase[0:13:2]) # => intervalo(step) na exibição
print(frase[::-1]) # exbibe ao contrario

print(lista)
print(type(lista))
print(lista[-1]) # ultimo valor
print(lista[-1:-6:-1])