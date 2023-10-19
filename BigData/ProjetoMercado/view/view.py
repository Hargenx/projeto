import streamlit as st
import plotly.express as px

class VisualizacaoSupermercado:
    def exibir_pagina(self, df_filtrado, total_do_mes, margem_de_lucro_bruta):
        col1, col2 = st.columns(2)
        col3, col4, col5 = st.columns(3)

        fig_data = px.bar(df_filtrado, x="Date", y="Total", color="City", title="Faturamento por dia")
        col1.plotly_chart(fig_data, use_container_width=True)

        fig_produto = px.bar(df_filtrado, x="Date", y="Product line",
                          color="City", title="Faturamento por tipo de produto",
                          orientation="h")
        col2.plotly_chart(fig_produto, use_container_width=True)

        cidade_total = df_filtrado.groupby("City")[["Total"]].sum().reset_index()
        fig_cidade = px.bar(cidade_total, x="City", y="Total",
                           title="Faturamento por filial")
        col3.plotly_chart(fig_cidade, use_container_width=True)

        fig_tipo = px.pie(df_filtrado, values="Total", names="Payment",
                           title="Faturamento por forma de pagamento")
        col4.plotly_chart(fig_tipo, use_container_width=True)

        fig_margem_bruta = px.bar(df_filtrado, x="Mês", y="gross income", color="City", title="Margem de Lucro Bruta por Mês")
        col5.plotly_chart(fig_margem_bruta, use_container_width=True)

        st.write("Dados Analisados:")
        st.write(df_filtrado)

        st.write(f"Total do Mês: ${total_do_mes:,.2f}")

        st.write(f"Margem de Lucro Bruta Média: {margem_de_lucro_bruta:,.2f}%")

