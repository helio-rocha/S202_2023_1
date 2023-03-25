from writeAJson import writeAJson
from database import Database

class ProductAnalyzer:
    def __init__(self, db : Database):
        self.db = db
        
    def total_vendas_dia(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"}, # Desagrega em produtos
        {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, # Agrupa o total por dia
        {"$sort": {"_id": 1}} # Ordena pela data
    ])
        writeAJson(result,"total_vendas_dia")
        
    def prod_mais_vendido_compra(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"}, # Desagrega em produtos
        {"$group": {"_id":{"venda":"$cliente_id","descricao":"$produtos.descricao"},"quantidade":{"$sum":"$produtos.quantidade"}}}, # Agrupa por compra
        {"$sort": {"quantidade":-1}}, # Coloca em ordem decrescente da quantidade vendida
        {"$group": {"_id": "$_id.venda", "descricao": {"$first":"$_id.descricao"},"quantidade":{"$first":"$quantidade"}}}, # Pega somente o produto mais vendido por compra
        {"$sort": {"_id": 1}}, # Ordena pelo número do pedido
        ])
        writeAJson(result,"prod_mais_vendido_compra")
    
    def cliente_mais_gastou(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"}, # Desagrega em produtos
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, # Agrupa o total por cliente
        {"$sort": {"total": -1}}, # Ordena de maneira decrescente
        {"$limit": 1} # Pega só o primeiro, ou seja, o que mais gastou
    ])
        writeAJson(result,"cliente_mais_gastou")
        
    def vendas_maior_um(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"}, # Desagrega em produtos
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}}, # Agrupa os produtos pela quantidade vendida
        {"$match":{"total":{"$gt":1}}} # retorna somente os que venderam mais que um
    ])
        writeAJson(result,"vendas_maior_um")