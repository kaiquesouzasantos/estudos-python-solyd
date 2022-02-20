# ===================== Orientação a Objetos =====================
class Veiculo():
    def __init__(self,cor,rodas,marca,tanque): # __init__ => metodo inicial(construtor) # self => recursivo
        self.cor = cor # atribui o valor dos parametros á variavel da classe
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        self.out = cor,rodas,marca,tanque
    def abastecer(self,litros):
        if self.tanque + litros > 50:
            print('Erro: tanque cheio')
        else:
            self.tanque += litros
        