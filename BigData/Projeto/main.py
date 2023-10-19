# Importa a classe SupermarketController do arquivo controller.py e a biblioteca Streamlit
from controller.controller import SupermarketController
import streamlit as st

# Define a função principal do programa
def main():
    # Configura as opções da página do Streamlit com layout amplo
    st.set_page_config(layout="wide")
    # Define o caminho do arquivo de dados CSV
    data_path = "./supermarket_sales.csv"
    # Cria uma instância da classe SupermarketController, passando o caminho do arquivo de dados como argumento
    controller = SupermarketController(data_path)
    # Chama o método create_month_column() do modelo para criar a coluna "Month" nos dados
    controller.model.create_month_column()  # Adicione esta linha para criar a coluna "Month"
    # Cria um seletor de mês na barra lateral do Streamlit, com base nos meses únicos na coluna "Month" dos dados
    month = st.sidebar.selectbox("Mês", controller.model.df["Month"].unique())

    # Chama o método run() do controlador, passando o mês, o ano e o dia selecionados como argumentos
    controller.run(month)

# Verifica se o script está sendo executado diretamente como um programa principal
if __name__ == "__main__":
    # Chama a função principal main() quando o script é executado
    main()
