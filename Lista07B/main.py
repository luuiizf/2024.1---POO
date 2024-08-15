import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lista07B')))
from categoria import Categoria, Categorias
from cliente import Cliente, Clientes
from produto import Produto, Produtos
from view import View


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.Menu()
            if op == 1: UI.Menu_Clientes()
            elif op == 2: UI.Menu_Categorias()
            elif op == 3: UI.Menu_Produtos()

    @staticmethod
    def Menu():
        print("Menu Principal")
        print("1- Clientes")
        print("2- Categorias")
        print("3- Produtos")
        print("9- Sair")
        return int(input("Escolha uma opção: "))

    # Métodos para o menu de Clientes
    @staticmethod
    def Menu_Clientes():
        op = 0
        while op != 9:
            print("Menu de Clientes")
            print("1- Inserir Cliente")
            print("2- Listar Clientes")
            print("3- Atualizar Cliente")
            print("4- Excluir Cliente")
            print("9- Voltar ao Menu Principal")
            op = int(input("Escolha uma opção: "))
            if op == 1: UI.Cliente_Inserir()
            elif op == 2: UI.Cliente_Listar()
            elif op == 3: UI.Cliente_Atualizar()
            elif op == 4: UI.Cliente_Excluir()

    @staticmethod
    def Cliente_Listar():
        clientes = View.Cliente_Listar()
        for cliente in clientes:
            print(cliente)

    @staticmethod
    def Cliente_Inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        View.Cliente_Inserir(nome, email, fone)

    @staticmethod
    def Cliente_Atualizar():
        UI.Cliente_Listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        View.Cliente_Atualizar(id, nome, email, fone)

    @staticmethod
    def Cliente_Excluir():
        UI.Cliente_Listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.Cliente_Excluir(id)

    # Métodos para o menu de Categorias
    @staticmethod
    def Menu_Categorias():
        op = 0
        while op != 9:
            print("Menu de Categorias")
            print("1- Inserir Categoria")
            print("2- Listar Categorias")
            print("3- Atualizar Categoria")
            print("4- Excluir Categoria")
            print("9- Voltar ao Menu Principal")
            op = int(input("Escolha uma opção: "))
            if op == 1: UI.Categoria_Inserir()
            elif op == 2: UI.Categoria_Listar()
            elif op == 3: UI.Categoria_Atualizar()
            elif op == 4: UI.Categoria_Excluir()

    @staticmethod
    def Categoria_Listar():
        categorias = View.Categoria_Listar()
        for categoria in categorias:
            print(categoria)

    @staticmethod
    def Categoria_Inserir():
        descricao = input("Informe a descrição da categoria: ")
        View.Categoria_Inserir(descricao)

    @staticmethod
    def Categoria_Atualizar():
        UI.Categoria_Listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        View.Categoria_Atualizar(id, descricao)

    @staticmethod
    def Categoria_Excluir():
        UI.Categoria_Listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.Categoria_Excluir(id)

    # Métodos para o menu de Produtos
    @staticmethod
    def Menu_Produtos():
        op = 0
        while op != 9:
            print("Menu de Produtos")
            print("1- Inserir Produto")
            print("2- Listar Produtos")
            print("3- Atualizar Produto")
            print("4- Excluir Produto")
            print("5- Reajustar Preços")
            print("9- Voltar ao Menu Principal")
            op = int(input("Escolha uma opção: "))
            if op == 1: UI.Produto_Inserir()
            elif op == 2: UI.Produto_Listar()
            elif op == 3: UI.Produto_Atualizar()
            elif op == 4: UI.Produto_Excluir()
            elif op == 5: UI.Produto_Reajustar()

    @staticmethod
    def Produto_Listar():
        produtos = View.Produto_Listar()
        for produto in produtos:
            print(produto)

    @staticmethod
    def Produto_Inserir():
        descricao = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço do produto: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        id_categoria = int(input("Informe o id da categoria do produto: "))
        View.Produto_Inserir(descricao, preco, estoque, id_categoria)

    @staticmethod
    def Produto_Atualizar():
        UI.Produto_Listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe a nova quantidade em estoque: "))
        id_categoria = int(input("Informe o novo id da categoria: "))
        View.Produto_Atualizar(id, descricao, preco, estoque, id_categoria)

    @staticmethod
    def Produto_Excluir():
        UI.Produto_Listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.Produto_Excluir(id)

    @staticmethod
    def Produto_Reajustar():
        percentual = float(input("Informe o percentual de reajuste: "))
        View.Produto_Reajustar(percentual)
        print("Preços reajustados com sucesso!")

UI.main()