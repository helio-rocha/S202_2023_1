
class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, id):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def create_partida(self, id):
        query = "CREATE (:Partida {id: $id})"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)
        
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_partidas(self):
        query = "MATCH (p:Partida) RETURN p.id AS id"
        results = self.db.execute_query(query)
        return [result["id"] for result in results]
    
    def get_partida(self, id):
        query = "MATCH (a:Player)-[r:PARTICIPA]->(p:Partida {id: $id}) RETURN a.name AS name, r.pontuacao AS pontuacao "
        parameters = {"id": id}
        results = self.db.execute_query(query,parameters)
        return [(result["name"], result["pontuacao"]) for result in results]
    
    def get_historico(self, name):
        query = "MATCH (a:Player {name: $name})-[r:PARTICIPA]->(p:Partida) RETURN p.id AS id_partida, r.pontuacao AS pontuacao "
        parameters = {"name": name}
        results = self.db.execute_query(query,parameters)
        return [(result["id_partida"], result["pontuacao"]) for result in results]

    def get_resultados(self):
        query = "MATCH (a:Player)-[r:PARTICIPA]->(p:Partida) RETURN a.name AS name, p.id AS id_partida, r.pontuacao AS pontuacao "
        results = self.db.execute_query(query)
        return [(result["name"], result["id_partida"], result["pontuacao"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def update_partida(self, old_id, new_id):
        query = "MATCH (p:Partida {id: $old_id}) SET p.id = $new_id"
        parameters = {"old_id": old_id, "new_id": new_id}
        self.db.execute_query(query, parameters)
        
    def update_resultado(self, player_name, id_partida, pontuacao):
        query = "MATCH (a:Player {name: $player_name})-[p:PARTICIPA]->(b:Partida {id: $id_partida}) SET p.pontuacao = $pontuacao"
        parameters = {"player_name": player_name, "id_partida": id_partida, "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)
        
    def insert_player_partida(self, player_name, id_partida, pontuacao):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Partida {id: $id_partida}) CREATE (a)-[:PARTICIPA {pontuacao: $pontuacao}]->(b)"
        parameters = {"player_name": player_name, "id_partida": id_partida, "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)

    def delete_partida(self, id):
        query = "MATCH (p:Partida {id: $id}) DETACH DELETE p"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (a:Player {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_resultado(self, player_name, id_partida):
        query = "MATCH (a:Player {name: $player_name})-[p:PARTICIPA]->(b:Partida {id: $id_partida}) DETACH DELETE p"
        parameters = {"player_name": player_name, "id_partida": id_partida,}
        self.db.execute_query(query, parameters)