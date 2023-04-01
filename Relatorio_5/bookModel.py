class BookModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, id: int, titulo: str, autor:str, ano:int, preco:float):
        try:
            res = self.db.collection.insert_one({"_id": id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_book_by_id(self, id: int):
        try:
            res = self.db.collection.find_one({"_id": id})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o livro: {e}")
            return None

    def update_book(self, id: int, titulo: str, autor:str, ano:int, preco:float):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documentos atualizados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_book(self, id: int):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print(f"Livro deletado: {res.deleted_count} documentos deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None