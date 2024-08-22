import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ProjetoTeste/models/')))
from categoria import Categoria, Categorias
from cliente import Cliente, Clientes
from produto import Produto, Produtos

class View:
    @staticmethod
    def Cliente_Listar():
        return Clientes.Listar()

    @staticmethod
    def Cliente_Inserir(nome, email, fone):
        id_cliente = max([cliente.get_id() for cliente in Clientes.Listar()], default=0) + 1
        cliente = Cliente(id_cliente, nome, email, fone)
        Clientes.Inserir(cliente)
        Clientes.Salvar()

    @staticmethod
    def Cliente_Atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Clientes.Atualizar(cliente)
        Clientes.Salvar()

    @staticmethod
    def Cliente_Excluir(id):
        cliente = Clientes.Listar_Id(id)
        if cliente:
            Clientes.Excluir(cliente)
            Clientes.Salvar()

    @staticmethod
    def Categoria_Listar():
        return Categorias.Listar()

    @staticmethod
    def Categoria_Inserir(descricao):
        id_categoria = max([categoria.get_id() for categoria in Categorias.Listar()], default=0) + 1
        categoria = Categoria(id_categoria, descricao)
        Categorias.Inserir(categoria)
        Categorias.Salvar()

    @staticmethod
    def Categoria_Atualizar(id, descricao):
        categoria = Categoria(id, descricao)
        Categorias.Atualizar(categoria)
        Categorias.Salvar()

    @staticmethod
    def Categoria_Excluir(id):
        categoria = Categorias.Listar_Id(id)
        if categoria:
            Categorias.Excluir(categoria)
            Categorias.Salvar()

    @staticmethod
    def Produto_Listar():
        return Produtos.Listar()

    @staticmethod
    def Produto_Inserir(descricao, preco, estoque, idCategoria):
        id_produto = max([produto.get_id() for produto in Produtos.Listar()], default=0) + 1
        produto = Produto(id_produto, descricao, preco, estoque, idCategoria)
        Produtos.Inserir(produto)
        Produtos.Salvar()

    @staticmethod
    def Produto_Atualizar(id, descricao, preco, estoque, idCategoria):
        produto = Produto(id, descricao, preco, estoque, idCategoria)
        Produtos.Atualizar(produto)
        Produtos.Salvar()

    @staticmethod
    def Produto_Excluir(id):
        produto = Produtos.Listar_Id(id)
        if produto:
            Produtos.Excluir(produto)
            Produtos.Salvar()

    @staticmethod
    def Produto_Reajustar(percentual):
        for produto in Produtos.Listar():
            produto.set_preco(produto.get_preco() * (1 + percentual / 100))
        Produtos.Salvar()
