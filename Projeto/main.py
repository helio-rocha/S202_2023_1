from database import Database
from vendasDAO import VendasDAO
from cli import VendasCLI

db = Database(database="Vendas", collection="Vendas")
vendasDAO = VendasDAO(db=db)

vendasCLI = VendasCLI(vendasDAO)
vendasCLI.run()
