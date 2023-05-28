from teacher_crud import TeacherCRUD

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "sair":
                print("Tchau!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente Novamente")

class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD: TeacherCRUD):
        super().__init__()
        self.teacherCRUD = teacherCRUD
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        name = input("Entre com o nome do professor: ")
        ano_nasc = int(input("Entre com o ano de nascimento do professor: "))
        cpf = input("Entre com o cpf do professor: ")
        print()
        self.teacherCRUD.create(name,ano_nasc,cpf)
        

    def read(self):
        name = input("Entre com o nome do professor: ")
        
        teacher = self.teacherCRUD.read(name)
        print()
        if teacher:
            print("Nome: " + teacher[0][0])
            print("Ano de Nascimento: " + str(teacher[0][1]))
            print("CPF: " + teacher[0][2])
        else:
            print("Não foi encontrado nenhum professor com esse nome")
        print()

    def update(self):
        name = input("Entre com o nome do professor: ")
        cpf = input("Entre com o cpf do professor: ")
        print()
        self.teacherCRUD.update(name,cpf)

    def delete(self):
        name = input("Entre com o nome do professor: ")
        print()
        self.teacherCRUD.delete(name)
        
    def run(self):
        print("Bem vindo")
        print("Comandos disponíveis: create, read, update, delete, sair")
        super().run()
        
