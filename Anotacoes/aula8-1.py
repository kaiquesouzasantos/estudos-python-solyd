# ===================== Orientação a Objetos =====================
from Veiculo import Veiculo # from ARQUIVO import CLASSE
from Carro import Carro

caminhao_rosa = Veiculo('rosa ',6,'ford ',10)  
carro_azul = Carro('azul ',4,'bmw ',30)
print(caminhao_rosa.out)
print(carro_azul.out)

carro_azul.abastecer(35)
caminhao_rosa.abastecer(70)

print(carro_azul.tanque) 
print(caminhao_rosa.tanque)
print(type(caminhao_rosa)) # variavel = objeto
print(type(carro_azul))