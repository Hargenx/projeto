# Importa as bibliotecas Streamlit e Plotly Express para criar a interface do usuário e os gráficos interativos
import streamlit as st
import plotly.express as px

# Define a classe SupermarketView, que é responsável por exibir a interface do usuário
class SupermarketView:
    # Método display_page que recebe os dados filtrados como argumento e cria a interface do usuário
    def display_page(self, df_filtered):
        # Divide a página em duas colunas
        col1, col2 = st.columns(2)
        # Divide a página em três colunas
        col3, col4, col5 = st.columns(3)

        # Cria um gráfico de barras usando Plotly Express para exibir o faturamento por dia
        fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
        # Exibe o gráfico na primeira coluna
        col1.plotly_chart(fig_date, use_container_width=True)

        # Cria um gráfico de barras horizontais para exibir o faturamento por tipo de produto
        fig_prod = px.bar(df_filtered, x="Date", y="Product line",
                          color="City", title="Faturamento por tipo de produto",
                          orientation="h")
        # Exibe o gráfico na segunda coluna
        col2.plotly_chart(fig_prod, use_container_width=True)

        # Calcula o faturamento total por filial e cria um gráfico de barras
        city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
        fig_city = px.bar(city_total, x="City", y="Total",
                           title="Faturamento por filial")
        # Exibe o gráfico na terceira coluna
        col3.plotly_chart(fig_city, use_container_width=True)

        # Cria um gráfico de pizza para exibir o faturamento por tipo de pagamento
        fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                           title="Faturamento por tipo de pagamento")
        # Exibe o gráfico na quarta coluna
        col4.plotly_chart(fig_kind, use_container_width=True)

        # Calcula a avaliação média por filial e cria um gráfico de barras
        city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
        fig_rating = px.bar(df_filtered, y="Rating", x="City",
                            title="Avaliação")
        # Exibe o gráfico na quinta coluna
        col5.plotly_chart(fig_rating, use_container_width=True)

        # Exibe os dados brutos do arquivo CSV
        st.write("Dados do arquivo CSV:")
        st.write(df_filtered)

        # Exibe os dados analisados
        st.write("Dados analisados:")
        st.write(df_filtered)  # Exibe os dados filtrados
        
        # Exibe uma lista dos itens analisados
        st.write("Itens analisados:")
        st.write("- Faturamento por dia")
        st.write("- Faturamento por tipo de produto")
        st.write("- Faturamento por filial")
        st.write("- Faturamento por tipo de pagamento")
        st.write("- Avaliação")