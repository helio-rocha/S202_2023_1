from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.207.138.216:7687", "neo4j", "landings-programs-highway")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com     o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("João",1)
game_db.create_player("Maria",2)
game_db.create_player("José",3)

# Criando algumas partidas
game_db.create_partida(1)
game_db.create_partida(2)
game_db.create_partida(3)

# Inserindo alguns jogadores nas partidas
game_db.insert_player_partida("João", 1, 10)
game_db.insert_player_partida("Maria", 1, 5)
game_db.insert_player_partida("José", 1, 3)

game_db.insert_player_partida("João", 2, 7)
game_db.insert_player_partida("Maria", 2, 9)

game_db.insert_player_partida("João", 3, 5)
game_db.insert_player_partida("José", 3, 5)

# Atualizando o id de uma partida
game_db.update_partida(3, 4)

# Atualizando o nome de um jogador
game_db.update_player("João", "Carlos")

# Deletando um jogador, uma partida e um relacionamento entre players e partidas
game_db.delete_player("Maria")
game_db.delete_partida(2)
game_db.delete_resultado("José",4)

# Pega informações de uma partida específica
print()
print("Informações da partida 1")
info = game_db.get_partida(1)
for player, pontuacao in info:
    print("O player",player,"fez",pontuacao,"pontos")

# Pega histórico de partidas de um jogador
print()
print("Histórico do jogador Carlos:")
hist = game_db.get_historico("Carlos")
for partida, pontuacao in hist:
    print("Na partida",partida,"fez",pontuacao,"pontos")

# Imprimindo todas as informações do banco de dados
print()
print("Players:")
print(game_db.get_players())
print()
print("Partidas:")
print(game_db.get_partidas())
print()
print("Resultados:")
result = game_db.get_resultados()
for player, partida, pontuacao in result:
    print("O player",player,"fez",pontuacao,"pontos na partida",partida)

# Fechando a conexão com o banco de dados
db.close()