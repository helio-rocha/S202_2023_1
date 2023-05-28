from database import Database
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.83.151.183:7687", "neo4j", "ribs-folder-tongue")
# db.drop_all()

# Criando uma instância da classe TeacherCRUD para interagir com o banco de dados
teacher_db = TeacherCRUD(db)
# 
# Criando Teacher
teacher_db.create('Chris Lima', 1956, '189.052.396-66')

# Procurando Teacher
teacher = teacher_db.read('Chris Lima')
if teacher:
    print("Nome: " + teacher[0][0])
    print("Ano de Nascimento: " + str(teacher[0][1]))
    print("CPF: " + teacher[0][2])
else:
    print("Não foi encontrado nenhum professor com esse nome")

# Atualizando um Teacher
teacher_db.update('Chris Lima','162.052.777-77')

# CLI
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

# Fechando a conexão com o banco de dados
db.close()