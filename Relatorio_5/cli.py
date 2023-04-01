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

class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        id = int(input("Entre com o id: "))
        titulo = input("Entre com o título: ")
        autor = input("Entre com o autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preço: "))
        self.book_model.create_book(id, titulo, autor, ano, preco)

    def read_book(self):
        id = int(input("Entre com o Id: "))
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Título: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preço: {book['preco']}")

    def update_book(self):
        id = int(input("Entre com o id: "))
        titulo = input("Entre com o novo título: ")
        autor = input("Entre com o novo autor: ")
        ano = int(input("Entre com o novo ano: "))
        preco = float(input("Entre com o novo preço: "))
        self.book_model.update_book(id, titulo, autor, ano, preco)

    def delete_book(self):
        id = int(input("Entre com o id: "))
        self.book_model.delete_book(id)
        
    def run(self):
        print("Biblioteca")
        print("Comandos disponíveis: create, read, update, delete, sair")
        super().run()
        
