import json

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self._id = id
        self._descricao = descricao
        self._preco = preco
        self._estoque = estoque
        self._idCategoria = id_categoria
     
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao
    
    def get_preco(self):
        return self._preco
    
    def set_preco(self, preco):
        self._preco = preco
    
    def get_estoque(self):
        return self._estoque
    
    def set_estoque(self, estoque):
        self._estoque = estoque
    
    def get_idCategoria(self):
        return self._idCategoria
    
    def set_idCategoria(self, idCategoria):
        self._idCategoria = idCategoria
    
    def __str__(self):
        return f"Produto (ID: {self._id}, Descrição: {self._descricao}, Preço: {self._preco}, Estoque: {self._estoque}, ID Categoria: {self._idCategoria})"


class Produtos:
    objetos = []

    @staticmethod
    def Inserir(obj):
        Produtos.objetos.append(obj)

    @staticmethod
    def Listar():
        return Produtos.objetos

    @staticmethod
    def Listar_Id(id):
        for produto in Produtos.objetos:
            if produto.get_id() == id:
                return produto
        return None

    @staticmethod
    def Atualizar(obj):
        for i, produto in enumerate(Produtos.objetos):
            if produto.get_id() == obj.get_id():
                Produtos.objetos[i] = obj
                break

    @staticmethod
    def Excluir(obj):
        Produtos.objetos = [produto for produto in Produtos.objetos if produto.get_id() != obj.get_id()]

    @staticmethod
    def Abrir():
        try:
            with open('produtos.json', 'r') as file:
                data = json.load(file)
                Produtos.objetos = [Produto(**item) for item in data]
        except FileNotFoundError:
            Produtos.objetos = []

    @staticmethod
    def Salvar():
        with open('produtos.json', 'w') as file:
            data = [produto.__dict__ for produto in Produtos.objetos]
            json.dump(data, file, default=str)