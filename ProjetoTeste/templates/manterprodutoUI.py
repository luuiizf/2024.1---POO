import streamlit as st
import pandas as pd
from views import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.Produto_Listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []  # lista de dicionários, onde cada dicionário é um produto
            for obj in produtos:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição do produto")
        preco = st.number_input("Informe o preço do produto", format="%.2f")
        estoque = st.number_input("Informe o estoque do produto", min_value=0)
        categorias = View.Categoria_Listar()
        if len(categorias) > 0:
            idCategoria = st.selectbox("Selecione a categoria do produto", [c.get_id() for c in categorias])
        else:
            st.warning("Nenhuma categoria cadastrada. Cadastre uma categoria primeiro.")
            return

        if st.button("Inserir"):
            View.Produto_Inserir(descricao, preco, estoque, idCategoria)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produtos = View.Produto_Listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            preco = st.number_input("Informe o novo preço", value=op.get_preco(), format="%.2f")
            estoque = st.number_input("Informe o novo estoque", value=op.get_estoque(), min_value=0)
            categorias = View.Categoria_Listar()
            if len(categorias) > 0:
                idCategoria = st.selectbox("Selecione a nova categoria", [c.get_id() for c in categorias])
            else:
                st.warning("Nenhuma categoria cadastrada.")
                return

            if st.button("Atualizar"):
                id = op.get_id()
                View.Produto_Atualizar(id, descricao, preco, estoque, idCategoria)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = View.Produto_Listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos)
            if st.button("Excluir"):
                id = op.get_id()
                View.Produto_Excluir(id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()
