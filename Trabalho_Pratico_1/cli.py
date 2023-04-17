from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

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

class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        passageiro = self.create_passageiro()
        corridas = []
        corridas.append(self.create_corrida(passageiro))
        op = input("Digite S se deseja criar outra corrida e N se não deseja criar outra corrida:")
        while(op not in ['S','N']):
            op = input("As opções existentes são somente S e N (Maísculo):")
        while(op == 'S'):
           corridas.append(self.create_corrida(passageiro))
           op = input("Digite S se deseja criar outra corrida e N se não deseja criar outra corrida:")
           while(op not in ['S','N']):
            op = input("As opções existentes são somente S e N (Maísculo):")
        nota_motorista = int(input("Entre com a nota do motorista: "))
        
        motorista = Motorista(corridas,nota_motorista)
        self.motoristaDAO.create_motorista(motorista)
        
    def create_passageiro(self):
        nome_passageiro = input("Entre com o nome do passageiro: ")
        documento_passageiro = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro,documento_passageiro)
        return passageiro
    
    def create_corrida(self,passageiro:Passageiro):
        nota_corrida = int(input("Entre com a nota da corrida: "))
        distancia_corrida = float(input("Entre com a distância da corrida: "))
        valor_corrida = float(input("Entre com o valor da corrida: "))
        corrida = Corrida(nota_corrida,distancia_corrida,valor_corrida,passageiro)
        return corrida

    def read_motorista(self):
        id = input("Entre com o Id: ")
        motorista = self.motoristaDAO.read_motorista_by_id(id=id)
        if motorista:
            print("Nota: " + str(motorista['nota']))
            i = 1
            for corrida in motorista["corridas"]:
                print()
                print("Corrida " + str(i))
                print("Nota da corrida: " + str(corrida["nota"]))
                print("Distância da corrida: " + str(corrida["distancia"]))
                print("Valor da corrida: " + str(corrida["valor"]))
                print("Nome do passageiro: " + str(corrida["passageiro"]["nome"]))
                print("Documento do passageiro: " + str(corrida["passageiro"]["documento"]))
                i = i + 1
        else:
            print("Não foi encontrado nenhum motorista com esse id")

    def update_motorista(self):
        id = str(input("Entre com o id do motorista em que se deseja fazer a alteração: "))
        passageiro = self.create_passageiro()
        corridas = []
        corridas.append(self.create_corrida(passageiro))
        op = input("Digite S se deseja criar outra corrida e N se não deseja criar outra corrida:")
        while(op not in ['S','N']):
            op = input("As opções existentes são somente S e N (Maísculo):")
        while(op == 'S'):
           corridas.append(self.create_corrida(passageiro))
           op = input("Digite S se deseja criar outra corrida e N se não deseja criar outra corrida:")
           while(op not in ['S','N']):
            op = input("As opções existentes são somente S e N (Maísculo):")
        nota_motorista = int(input("Entre com a nota do motorista: "))
        
        motorista = Motorista(corridas,nota_motorista)
        self.motoristaDAO.update_motorista(id, motorista)

    def delete_motorista(self):
        id = str(input("Entre com o id: "))
        self.motoristaDAO.delete_motorista(id)
        
    def run(self):
        print("Bem vindo")
        print("Comandos disponíveis: create, read, update, delete, sair")
        super().run()
        
