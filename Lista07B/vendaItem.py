import json

class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self._id = id
        self._qtd = qtd
        self._preco = preco
        self._idVenda = idVenda
        self._idProduto = idProduto
    
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_qtd(self):
        return self._qtd
    
    def set_qtd(self, qtd):
        self._qtd = qtd
    
    def get_preco(self):
        return self._preco
    
    def set_preco(self, preco):
        self._preco = preco
    
    def get_idVenda(self):
        return self._idVenda
    
    def set_idVenda(self, idVenda):
        self._idVenda = idVenda
    
    def get_idProduto(self):
        return self._idProduto
    
    def set_idProduto(self, idProduto):
        self._idProduto = idProduto

    def __str__(self):
        return f"Venda de Item (ID: {self._id}, Quantidade: {self._qtd}, Preço: {self._preco}, ID Venda: {self._idVenda}, ID Produto: {self._idProduto})"


class VendaItens:
    objetos = []

    @staticmethod
    def Inserir(obj):
        VendaItens.objetos.append(obj)

    @staticmethod
    def Listar():
        return VendaItens.objetos

    @staticmethod
    def Listar_Id(id):
        for vendaItem in VendaItens.objetos:
            if vendaItem.get_id() == id:
                return vendaItem
        return None

    @staticmethod
    def Atualizar(obj):
        for i, vendaItem in enumerate(VendaItens.objetos):
            if vendaItem.get_id() == obj.get_id():
                VendaItens.objetos[i] = obj
                break

    @staticmethod
    def Excluir(obj):
        VendaItens.objetos = [vendaItem for vendaItem in VendaItens.objetos if vendaItem.get_id() != obj.get_id()]

    @staticmethod
    def Abrir():
        try:
            with open('vendaitens.json', 'r') as file:
                data = json.load(file)
                VendaItens.objetos = [VendaItem(**item) for item in data]
        except FileNotFoundError:
            VendaItens.objetos = []

    @staticmethod
    def Salvar():
        with open('vendaitens.json', 'w') as file:
            data = [vendaItem.__dict__ for vendaItem in VendaItens.objetos]
            json.dump(data, file, default=str)