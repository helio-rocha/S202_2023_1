from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")

pokedex = Pokedex(db)

pokedex.weak_fire()
pokedex.no_evolution()
pokedex.basic_weak_water()
pokedex.basic_eletric()
pokedex.psy()