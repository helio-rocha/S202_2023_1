from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="Taxi", collection="Motoristas")
motoristaDAO = MotoristaDAO(db=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()
