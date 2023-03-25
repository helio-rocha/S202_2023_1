from database import Database
from product_analyser import ProductAnalyzer

db = Database(database="mercado", collection="compras")
# db.resetDatabase()

product_analyser = ProductAnalyzer(db)

product_analyser.total_vendas_dia()
product_analyser.prod_mais_vendido_compra()
product_analyser.cliente_mais_gastou()
product_analyser.vendas_maior_um()

