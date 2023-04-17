from database import Database
from motorista import Motorista
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, db : Database):
        self.db = db
        
    def create_motorista(self, motorista:Motorista):
        doc = {
    "nota": motorista.nota,
    "corridas":
        [
        
        ]
    }
        for corrida in motorista.corridas:
            doc["corridas"].append({
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro":
                {
                    "nome": corrida.passageiro.nome,
                    "documento" : corrida.passageiro.documento
                }
            }
            )
        try:
            res = self.db.collection.insert_one(doc)
            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            # print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o motorista: {e}")
            return None

    def update_motorista(self, id, motorista:Motorista):
        doc = {
    "nota": motorista.nota,
    "corridas":
        [
        
        ]
    }
        for corrida in motorista.corridas:
            doc["corridas"].append({
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro":
                {
                    "nome": corrida.passageiro.nome,
                    "documento" : corrida.passageiro.documento
                }
            }
            )
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": doc})
            print(f"Motorista atualizado: {res.modified_count} documentos atualizados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documentos deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
        
        
