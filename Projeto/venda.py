from vendedor import Vendedor
from comprador import Comprador

class Venda:
    def __init__(self,comprador:Comprador,vendedor:Vendedor,valor:float):
        self.comprador = comprador
        self.vendedor = vendedor
        self.valor = valor
