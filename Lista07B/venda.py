import json

from datetime import datetime

class Venda:
    def __init__(self, id, data, carrinho=False, total=0.0, idCliente=None):
        self._id = id
        self._data = datetime.fromisoformat(data) if isinstance(data, str) else data
        self._carrinho = carrinho
        self._total = total
        self._idCliente = idCliente

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data
    
    def get_carrinho(self):
        return self._carrinho
    
    def set_carrinho(self, carrinho):
        self._carrinho = carrinho
    
    def get_total(self):
        return self._total
    
    def set_total(self, total):
        self._total = total
    
    def get_idCliente(self):
        return self._idCliente
    
    def set_idCliente(self, idCliente):
        self._idCliente = idCliente

    def __str__(self):
        return f"Venda[ID: {self._id}, Data: {self._data}, Carrinho: {self._carrinho}, Total: {self._total}, ID Cliente: {self._idCliente}]"


class Vendas:
    objetos = []

    @staticmethod
    def Inserir(obj):
        Vendas.objetos.append(obj)

    @staticmethod
    def Listar():
        return Vendas.objetos

    @staticmethod
    def Listar_Id(id):
        for venda in Vendas.objetos:
            if venda.get_id() == id:
                return venda
        return None

    @staticmethod
    def Atualizar(obj):
        for i, venda in enumerate(Vendas.objetos):
            if venda.get_id() == obj.get_id():
                Vendas.objetos[i] = obj
                break

    @staticmethod
    def Excluir(obj):
        Vendas.objetos = [venda for venda in Vendas.objetos if venda.get_id() != obj.get_id()]

    @staticmethod
    def Abrir():
        try:
            with open('vendas.json', 'r') as file:
                data = json.load(file)
                Vendas.objetos = [Venda(**item) for item in data]
        except FileNotFoundError:
            Vendas.objetos = []

    @staticmethod
    def Salvar():
        with open('vendas.json', 'w') as file:
            data = [venda.__dict__ for venda in Vendas.objetos]
            json.dump(data, file, default=str)