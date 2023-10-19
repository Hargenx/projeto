import streamlit as st
from controller.controller import ControladorSupermercado

def main(caminho):
    st.set_page_config(layout="wide") 
    controlador = ControladorSupermercado(caminho)
    controlador.modelo.criar_coluna_mes()
    mes = st.sidebar.selectbox("Mês", controlador.modelo.df["Mês"].unique())
    controlador.executar(mes)

if __name__ == "__main__":
    main("supermarket_sales.csv")
