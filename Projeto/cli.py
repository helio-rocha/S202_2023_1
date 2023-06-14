from comprador import Comprador
from vendedor import Vendedor
from venda import Venda
from vendasDAO import VendasDAO

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

class VendasCLI(SimpleCLI):
    def __init__(self, vendasDAO: VendasDAO):
        super().__init__()
        self.vendasDAO = vendasDAO
        self.add_command("create", self.create_venda)
        self.add_command("read", self.read_venda)
        self.add_command("update", self.update_venda)
        self.add_command("delete", self.delete_venda)

    def create_vendedor(self):
        nome_vendedor = input("Entre com o nome do vendedor: ")
        empresa_vendedor = input("Entre com a empresa do vendedor: ")
        vendedor = Vendedor(nome_vendedor,empresa_vendedor)
        return vendedor
        
    def create_comprador(self):
        nome_comprador = input("Entre com o nome do comprador: ")
        documento_comprador = input("Entre com o documento do comprador: ")
        comprador = Comprador(nome_comprador,documento_comprador)
        return comprador
    
    def create_venda(self):
        valor = float(input("Entre com o valor da venda: "))
        comprador = self.create_comprador()
        vendedor = self.create_vendedor()
        venda = Venda(comprador, vendedor, valor)
        self.vendasDAO.create_venda(venda)
        

    def read_venda(self):
        op = input("Se deseja procurar por vendedor aperte V, se deseja procurar por comprador aperte C: ")
        while not(op == 'V' or op == 'C'):
            op = input("Opção inválida. Tente Novamente ")
        nome = input("Entre com o nome: ")
        venda = self.vendasDAO.read_venda(nome,op)
        print()
        if venda:
            print("Nome do vendedor: " + str(venda['vendedor']['nome']))
            print("Empresa do vendedor: " + str(venda['vendedor']['empresa']))
            print("Nome do comprador: " + str(venda["comprador"]["nome"]))
            print("Documento do comprador: " + str(venda["comprador"]["documento"]))
            print("Valor: " + str(venda['valor']))
        else:
            print("Não foi encontrado nenhuma venda associada a esse vendededor/comprador")
        print()

    def update_venda(self):
        op = input("Se deseja procurar por vendedor aperte V, se deseja procurar por comprador aperte C: ")
        while not(op == 'V' or op == 'C'):
            op = input("Opção inválida. Tente Novamente ")
        nome = input("Entre com o nome: ")
        venda = self.vendasDAO.read_venda(nome,op)
        if venda:
            valor = float(input("Entre com o valor da venda: "))
            comprador = self.create_comprador()
            vendedor = self.create_vendedor()
            venda = Venda(comprador, vendedor, valor)
            self.vendasDAO.update_venda(nome, venda, op)
        else:
            print("Não foi encontrado nenhuma venda associada a esse vendededor/comprador")

    def delete_venda(self):
        op = input("Se deseja procurar por vendedor aperte V, se deseja procurar por comprador aperte C: ")
        while not(op == 'V' or op == 'C'):
            op = input("Opção inválida. Tente Novamente ")
        nome = input("Entre com o nome: ")
        self.vendasDAO.delete_venda(nome,op)
        
    def run(self):
        print("Bem vindo")
        print("Comandos disponíveis: create, read, update, delete, sair")
        super().run()
        
