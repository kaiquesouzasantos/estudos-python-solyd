# ===================== Orientação a Objetos =====================
from Veiculo import Veiculo

class Carro(Veiculo): # (Veiculo) => herda a classe
    def __init__(self,cor,rodas,marca,tanque):
        Veiculo.__init__(self,cor,rodas,marca,tanque)
