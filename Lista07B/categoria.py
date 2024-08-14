import json

class Categoria:
    def __init__(self, id, descricao):
        self._id = id
        self._descricao = descricao

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao

    def __str__(self):
        return f"Categoria (ID: {self._id}, Descrição: {self._descricao})"


class Categorias:
    objetos = []

    @staticmethod
    def Inserir(obj):
        Categorias.objetos.append(obj)

    @staticmethod
    def Listar():
        return Categorias.objetos

    @staticmethod
    def Listar_Id(id):
        for categoria in Categorias.objetos:
            if categoria.get_id() == id:
                return categoria
        return None

    @staticmethod
    def Atualizar(obj):
        for i, categoria in enumerate(Categorias.objetos):
            if categoria.get_id() == obj.get_id():
                Categorias.objetos[i] = obj
                break

    @staticmethod
    def Excluir(obj):
        Categorias.objetos = [categoria for categoria in Categorias.objetos if categoria.get_id() != obj.get_id()]

    @staticmethod
    def Abrir():
        try:
            with open('categorias.json', 'r') as file:
                data = json.load(file)
                Categorias.objetos = [Categoria(**item) for item in data]
        except FileNotFoundError:
            Categorias.objetos = []

    @staticmethod
    def Salvar():
        with open('categorias.json', 'w') as file:
            data = [categoria.__dict__ for categoria in Categorias.objetos]
            json.dump(data, file, default=str)