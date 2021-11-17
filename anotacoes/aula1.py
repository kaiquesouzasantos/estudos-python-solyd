# ===================== type prints =====================
print('Hellow world') 
print('Segunda linha')

print('Hellow world\nSegunda linha') # \n => pula linha(quebra de linha)

print('Hellow world\tSegunda linha') # \t => tab

# ===================== type variaveis =====================
nome = 'Kaique' # string 
# nome = input('digite seu nome: ') 
idade = 15 # int
# idade = input('digite sua idade: ')
altura = 1.85 # float
# altura = ('digite sua altura: ')

print(nome,idade,altura)
print(type(nome),type(idade),type(altura)) # type() => tipo de dado

print(nome, 'tem', idade, 'anos e', altura, 'de altura') 
# , => concatenação, os tipos são convertidos automaticamente para string e tem espaçamento automatico

print(nome+' tem '+str(idade)+' anos e '+str(altura)+' de altura ') 
# + => concatenação, os tipos não são convertidos automaticamente para string e não tem espeçamento automatico || mais recomendado para utilização em variaveis
# str() => converte float e int em string
frase = (nome+' tem '+str(idade)+' anos e '+str(altura)+' de altura ')
print(frase)

# ===================== type operações =====================
print(10**2) # ** => exponencial 
print(16**(1/2)) # ** (1/2) => raiz quadrada