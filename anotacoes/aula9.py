# ===================== abrir texto(.txt) =====================
open('Caminho\NomeDoArvivo.[tipo_primitivo]') # open() => abrir arquivos em python # \ = \\ dentro
open('Caminho\NomeDoArvivo.[tipo_primitivo]','w') # 'w' => (w = write) cria o arquivo ou sobreescreve
open('Caminho\NomeDoArvivo.[tipo_primitivo]','r') # 'r' => (r = read) lê o arquivo 
open('Caminho\NomeDoArvivo.[tipo_primitivo]','r+') # 'r+' => escreve e lê o arquivo 
open('Caminho\NomeDoArvivo.[tipo_primitivo]','a') # 'a' => (a = append) cria(adiciona) o arquivo 
open('Caminho\NomeDoArvivo.png','rb') # => hexadecimal do arquivo

arquivo = open('Caminho\NomeDoArvivo.[tipo_primitivo]','w')
arquivo = open('Caminho\NomeDoArvivo.[tipo_primitivo]','r')
arquivo.write("texto que sera escrito dento do arquivo") # write() => metodo que escreve
print(arquivo.read()) # read() => metodo de leitura

for i in range(0,1001):
    arquivo.write(str(i)+" - ")

for linha in arquivo:
    print(linha)


# ===================== abrir bytes =====================
open('Caminho\NomeDoArvivo.[tipo_primitivo]','b')


