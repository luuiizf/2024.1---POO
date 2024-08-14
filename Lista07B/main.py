import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from Lista07B.categoria import Categoria, Categorias
from Lista07B.cliente import Cliente, Clientes
from Lista07B.produto import Produto, Produtos


class UI:
    @staticmethod
    def menu():
        print("Menu Principal")
        print("1- Clientes")
        print("2- Categorias")
        print("3- Produtos")
        print("9- Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def sub_menu(entity_name):
        print(f"{entity_name}")
        print("  1-Inserir")
        print("  2-Listar")
        print("  3-Atualizar")
        print("  4-Excluir")
        print("  9-Voltar ao menu principal")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.menu_clientes()
            if op == 2: UI.menu_categorias()
            if op == 3: UI.menu_produtos()

    @staticmethod
    def menu_clientes():
        op = 0
        while op != 9:
            op = UI.sub_menu("Clientes")
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

    @staticmethod
    def menu_categorias():
        op = 0
        while op != 9:
            op = UI.sub_menu("Categorias")
            if op == 1: UI.categoria_inserir()
            if op == 2: UI.categoria_listar()
            if op == 3: UI.categoria_atualizar()
            if op == 4: UI.categoria_excluir()

    @staticmethod
    def menu_produtos():
        op = 0
        while op != 9:
            op = UI.sub_menu("Produtos")
            if op == 1: UI.produto_inserir()
            if op == 2: UI.produto_listar()
            if op == 3: UI.produto_atualizar()
            if op == 4: UI.produto_excluir()

    # Métodos para clientes
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        id_cliente = max([cliente.get_id() for cliente in Clientes.Listar()], default=0) + 1
        cliente = Cliente(id_cliente, nome, email, fone)
        Clientes.Inserir(cliente)
        Clientes.Salvar()

    @staticmethod
    def cliente_listar():
        for cliente in Clientes.Listar(): 
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        cliente = Cliente(id, nome, email, fone)
        Clientes.Atualizar(cliente)
        Clientes.Salvar()

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        cliente = Clientes.Listar_Id(id)
        if cliente:
            Clientes.Excluir(cliente)
            Clientes.Salvar()

    # Métodos para categorias
    @staticmethod
    def categoria_inserir():
        descricao = input("Informe a descrição da categoria: ")
        id_categoria = max([categoria.get_id() for categoria in Categorias.Listar()], default=0) + 1
        categoria = Categoria(id_categoria, descricao)
        Categorias.Inserir(categoria)
        Categorias.Salvar()

    @staticmethod
    def categoria_listar():
        for categoria in Categorias.Listar():
            print(categoria)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        categoria = Categoria(id, descricao)
        Categorias.Atualizar(categoria)
        Categorias.Salvar()

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        categoria = Categorias.Listar_Id(id)
        if categoria:
            Categorias.Excluir(categoria)
            Categorias.Salvar()

    # Métodos para produtos
    @staticmethod
    def produto_inserir():
        descricao = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço do produto: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        id_categoria = int(input("Informe o id da categoria do produto: "))
        id_produto = max([produto.get_id() for produto in Produtos.Listar()], default=0) + 1
        produto = Produto(id_produto, descricao, preco, estoque, id_categoria)
        Produtos.Inserir(produto)
        Produtos.Salvar()

    @staticmethod
    def produto_listar():
        for produto in Produtos.Listar():
            print(produto)

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe a nova quantidade em estoque: "))
        id_categoria = int(input("Informe o novo id da categoria: "))
        produto = Produto(id, descricao, preco, estoque, id_categoria)
        Produtos.Atualizar(produto)
        Produtos.Salvar()

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        produto = Produtos.Listar_Id(id)
        if produto:
            Produtos.Excluir(produto)
            Produtos.Salvar()

UI.main()
