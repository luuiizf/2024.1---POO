import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_fone(self):
        return self._fone
    
    def set_fone(self, fone):
        self._fone = fone

    def __str__(self):
        return f"Cliente (ID: {self._id}, Nome: {self._nome}, Email: {self._email}, Fone: {self._fone})"

class Clientes:
    objetos = []

    @staticmethod
    def Inserir(obj):
        Clientes.objetos.append(obj)

    @staticmethod
    def Listar():
        return Clientes.objetos

    @staticmethod
    def Listar_Id(id):
        for cliente in Clientes.objetos:
            if cliente.get_id() == id:
                return cliente
        return None

    @staticmethod
    def Atualizar(obj):
        for i, cliente in enumerate(Clientes.objetos):
            if cliente.get_id() == obj.get_id():
                Clientes.objetos[i] = obj
                break

    @staticmethod
    def Excluir(obj):
        Clientes.objetos = [cliente for cliente in Clientes.objetos if cliente.get_id() != obj.get_id()]

    @staticmethod
    def Abrir():
        try:
            with open('clientes.json', 'r') as file:
                data = json.load(file)
                Clientes.objetos = [Cliente(**item) for item in data]
        except FileNotFoundError:
            Clientes.objetos = []

    @staticmethod
    def Salvar():
        with open('clientes.json', 'w') as file:
            data = [cliente.__dict__ for cliente in Clientes.objetos]
            json.dump(data, file, default=str)
    
