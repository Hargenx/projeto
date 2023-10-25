import streamlit as st
from controller.controller import ControladorSupermercado

def main(caminho): 
    controlador = ControladorSupermercado(caminho)
    controlador.modelo.criar_coluna_mes()
    #mes = st.sidebar.selectbox("Mês", controlador.modelo.df["Mes"].unique())
    st.sidebar.markdown(' :balloon: __Nossas opções__ :balloon: ')
    mes = st.sidebar.radio("Mês", controlador.modelo.df["Mes"].unique())
    controlador.executar(mes)
    st.sidebar.markdown('''Happy Streamlit-ing! :balloon:''')
    #controlador.executar(mes)

if __name__ == "__main__":
    st.set_page_config(page_title="Exemplo Final", page_icon="😊", layout="wide")
    main("./assets/supermarket_sales - sheet1.csv")