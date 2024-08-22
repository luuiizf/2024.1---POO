import streamlit as st
import pandas as pd
from views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        categorias = View.Categoria_Listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            dic = []  # lista de dicionários, onde cada dicionário é uma categoria
            for obj in categorias:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição")
        if st.button("Inserir"):
            View.Categoria_Inserir(descricao)
            st.success("Categoria inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.Categoria_Listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Categorias", categorias)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Categoria_Atualizar(id, descricao)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        categorias = View.Categoria_Listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categorias)
            if st.button("Excluir"):
                id = op.get_id()
                View.Categoria_Excluir(id)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
