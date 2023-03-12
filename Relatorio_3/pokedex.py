from helper.WriteAJson import writeAJson
from database import Database

class Pokedex:
    def __init__(self, db : Database):
        self.db = db
        
    def weak_fire(self): # Retorna todos os pokemons fracos contra fogo
        result = self.db.collection.find({"weaknesses": "Fire"})
        writeAJson(result,"weak_fire")
        
    def no_evolution(self): # Retorna todos os pokemons no máximo de suas evoluções
        result = self.db.collection.find({"next_evolution": {"$exists": False}})
        writeAJson(result,"no_evolution")
        
    def basic_weak_water(self): # Retorna todos os pokemons ainda não evoluidos fracos contra água
        result = self.db.collection.find({"prev_evolution": {"$exists": False},"weaknesses": "Water"})
        writeAJson(result,"basic_weak_water")
        
    def basic_eletric(self): # Retorna todos os pokemons ainda não evoluidos do tipo elétrico
        result = self.db.collection.find({"prev_evolution": {"$exists": False}, "type" : "Electric"})
        writeAJson(result,"basic_eletric")
        
    def psy(self): # Retorna todos os pokemons do tipo psiquico
        result = self.db.collection.find({"type" : "Psychic"})
        writeAJson(result,"psy")