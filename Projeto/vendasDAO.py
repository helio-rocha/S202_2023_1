from database import Database
from comprador import Comprador
from bson.objectid import ObjectId
from venda import Venda

class VendasDAO:
    def __init__(self, db : Database):
        self.db = db
        
    def create_venda(self, venda: Venda):
        doc = {
        "vendedor":
            {
                "nome": venda.vendedor.nome,
                "empresa": venda.vendedor.empresa
            },
        "comprador":
            {
                "nome": venda.comprador.nome,
                "documento": venda.comprador.documento
            },
        "valor": venda.valor
        }
        
        try:
            res = self.db.collection.insert_one(doc)
            print(f"Venda criada com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar a venda: {e}")
            return None

    def read_venda(self, nome: str, op: str):
        try:
            if op == 'V':
                res = self.db.collection.find_one({"vendedor.nome": nome})
            else:
                res = self.db.collection.find_one({"comprador.nome": nome})
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao procurar a venda: {e}")
            return None

    def update_venda(self, nome, venda: Venda, op: str):
        doc = {
            "vendedor":
                {
                    "nome": venda.vendedor.nome,
                    "empresa": venda.vendedor.empresa
                },
            "comprador":
                {
                    "nome": venda.comprador.nome,
                    "documento": venda.comprador.documento
                },
            "valor": venda.valor
            }
        try:
            if op == 'V':
                res = self.db.collection.update_one({"vendedor.nome": nome}, {"$set": doc})
            else:
                res = self.db.collection.update_one({"comprador.nome": nome}, {"$set": doc})
            print(f"Venda atualizado: {res.modified_count} documentos atualizados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar a venda: {e}")
            return None

    def delete_venda(self, nome: str, op: str):
        try:
            if op == 'V':
                res = self.db.collection.delete_one({"vendedor.nome": nome})
            else:
                res = self.db.collection.delete_one({"comprador.nome": nome})
            print(f"Venda deletada: {res.deleted_count} documentos deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a venda: {e}")
            return None