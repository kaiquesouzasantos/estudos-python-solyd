# ===================== type operadores =====================
var1 = True
var2 = False

print(type(var1),type(var2)) # boolean

if var1 == True: # : => chave
    print('Verdade!')
else: 
    print('Mentira!')

print(1==1) # comparação, retorna boolean
print(1==2) 
print(1>2)
print(1<2)
print(3!=2)

# and e or => comparação condicional 

print(1==2 or 2!=1)
print(1==2 and 2!=2)

if ((50>20) and ('abacaxi'=='abacaxi')) or 2==2:
    print('true')
else:
    print('false')

print('Menu:\n1 = escreve Kaique\n2 = escreve Kaique2\n3 = escreve Kaique3')
opcao = input("escolha uma opção: ")
if opcao == '1':
    print('Kaique')
elif opcao == '2':
    print('Kaique2')
elif opcao == '3': # elif => else if
    print('Kaique3')
else:
    print('Opção inválida!')

idade = 20
if idade == 50:
    print('True 50 anos')
else:
    print('Not 50 anos')

if not idade == 50:
    print('Not 50 anos')
else:
    print('True 50 anos')